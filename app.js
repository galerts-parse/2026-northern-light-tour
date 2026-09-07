// 2026 Northern Light Tour Application Script (AES Decryption Enabled)

let globalItineraryData = null;

document.addEventListener('DOMContentLoaded', () => {
  initPasswordProtection();
});

// Password Protection & AES Decryption (PIN: 8520)
function initPasswordProtection() {
  const authOverlay = document.getElementById('auth-overlay');
  const authModal = document.getElementById('auth-modal');
  const authSubmitBtn = document.getElementById('auth-submit-btn');
  const authErrorMsg = document.getElementById('auth-error-msg');
  const pinInputs = document.querySelectorAll('.pin-digit');

  if (!authOverlay) return;

  // Check saved session PIN
  const savedPin = sessionStorage.getItem('auth_pin');
  if (savedPin) {
    if (tryDecryptAndRender(savedPin)) {
      authOverlay.style.display = 'none';
      return;
    }
  }

  // Focus first digit input
  if (pinInputs.length > 0) {
    pinInputs[0].focus();
  }

  // Handle pin digit navigation
  pinInputs.forEach((input, idx) => {
    input.addEventListener('input', (e) => {
      const val = e.target.value;
      if (val && idx < pinInputs.length - 1) {
        pinInputs[idx + 1].focus();
      }
      if (idx === pinInputs.length - 1 && val) {
        verifyPin();
      }
    });

    input.addEventListener('keydown', (e) => {
      if (e.key === 'Backspace' && !input.value && idx > 0) {
        pinInputs[idx - 1].focus();
      }
      if (e.key === 'Enter') {
        verifyPin();
      }
    });
  });

  if (authSubmitBtn) {
    authSubmitBtn.addEventListener('click', verifyPin);
  }

  function verifyPin() {
    let enteredPin = '';
    pinInputs.forEach(i => enteredPin += i.value.trim());

    if (tryDecryptAndRender(enteredPin)) {
      sessionStorage.setItem('auth_passed', 'true');
      sessionStorage.setItem('auth_pin', enteredPin);
      authOverlay.style.display = 'none';
    } else {
      authErrorMsg.style.display = 'block';
      if (authModal) {
        authModal.classList.add('shake');
        setTimeout(() => authModal.classList.remove('shake'), 500);
      }
      pinInputs.forEach(i => i.value = '');
      if (pinInputs.length > 0) pinInputs[0].focus();
    }
  }
}

function tryDecryptAndRender(pin) {
  if (typeof encryptedItineraryData === 'undefined' || typeof CryptoJS === 'undefined') return false;

  try {
    const bytes = CryptoJS.AES.decrypt(encryptedItineraryData, pin);
    const decryptedText = bytes.toString(CryptoJS.enc.Utf8);
    
    if (decryptedText && decryptedText.trim().startsWith('[')) {
      globalItineraryData = JSON.parse(decryptedText);
      
      // Render whichever page view is active
      if (document.getElementById('map')) {
        initItineraryMap(globalItineraryData);
      }
      if (document.getElementById('tour-package-content')) {
        renderTourPackageCards(globalItineraryData);
      }
      return true;
    }
  } catch (e) {
    console.error('Decryption failed:', e);
  }
  return false;
}

// Map & Itinerary Application Logic for index.html
function initItineraryMap(itineraryData) {
  const mapElem = document.getElementById('map');
  const listElem = document.getElementById('itinerary-list');

  if (!mapElem || typeof L === 'undefined' || !itineraryData) return;

  // Clear existing elements if re-rendering
  if (listElem) listElem.innerHTML = '';

  // Initialize Leaflet Map centered on Lapland/Nordics
  const map = L.map('map').setView([65.8252, 23.6886], 5);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  const markers = [];
  const latLngs = [];

  itineraryData.forEach((day) => {
    latLngs.push(day.coords);

    let markerColor = '#2563eb';
    if (day.hotelStatus === 'confirmed') markerColor = '#16a34a';
    if (day.hotelStatus === 'shortlisted') markerColor = '#d97706';

    const customIcon = L.divIcon({
      className: 'custom-map-pin',
      html: `<div style="background-color:${markerColor}; color:white; font-weight:bold; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; border:2px solid white; box-shadow:0 2px 5px rgba(0,0,0,0.3); font-size:12px;">${day.day}</div>`,
      iconSize: [28, 28],
      iconAnchor: [14, 14]
    });

    const marker = L.marker(day.coords, { icon: customIcon }).addTo(map);
    
    const popupContent = `
      <div style="font-family:sans-serif; padding:5px;">
        <strong style="color:#0f172a; font-size:14px;">Day ${day.day}: ${day.title}</strong><br/>
        <span style="color:#64748b; font-size:12px;"><i class="fa-solid fa-location-dot"></i> ${day.location}</span><br/>
        <div style="margin-top:6px; font-size:12px;">
          <strong>Hotel:</strong> ${day.hotel}<br/>
          <strong>Ref:</strong> ${day.bookingRef}
        </div>
      </div>
    `;
    marker.bindPopup(popupContent);
    markers.push(marker);

    // Sidebar Item
    if (listElem) {
      const item = document.createElement('div');
      item.className = 'day-item';
      item.innerHTML = `
        <div class="day-item-header">
          <span class="day-item-title">Day ${day.day}: ${day.location.split(',')[0]}</span>
          <span class="day-item-date">${day.date}</span>
        </div>
        <div class="day-item-sub">${day.title}</div>
      `;

      item.addEventListener('click', () => {
        document.querySelectorAll('.day-item').forEach(el => el.classList.remove('active'));
        item.classList.add('active');
        map.flyTo(day.coords, 8, { duration: 1.2 });
        marker.openPopup();
      });

      listElem.appendChild(item);
    }
  });

  const polyline = L.polyline(latLngs, {
    color: '#2563eb',
    weight: 4,
    opacity: 0.8,
    dashArray: '8, 8'
  }).addTo(map);

  map.fitBounds(polyline.getBounds(), { padding: [40, 40] });
}

// Render Tour Package Cards for tour_package.html
function renderTourPackageCards(itineraryData) {
  const container = document.getElementById('tour-package-content');
  const navContainer = document.getElementById('sidebar-nav-ul');
  if (!container || !itineraryData) return;

  container.innerHTML = '';
  if (navContainer) navContainer.innerHTML = '';

  itineraryData.forEach((d) => {
    if (navContainer) {
      const li = document.createElement('li');
      li.innerHTML = `<a href="#day-${d.day}">Day ${d.day}: ${d.location.split(',')[0]}</a>`;
      navContainer.appendChild(li);
    }

    const statusCls = d.hotelStatus;
    const statusLabel = statusCls === 'confirmed' ? '✅ Confirmed' : (statusCls === 'shortlisted' ? '⚠️ Shortlisted' : '📌 Booking Pending');
    const tagsHtml = (d.tags || []).map(t => `<span class="chip">#${t}</span>`).join('');

    const card = document.createElement('div');
    card.id = `day-${d.day}`;
    card.className = 'day-card';
    card.innerHTML = `
      <div class="day-header">
        <div>
          <span style="color: #2563eb; font-weight: 700; font-size: 0.9rem;">DAY ${d.day} &bull; ${d.date}</span>
          <div class="day-title">${d.title}</div>
        </div>
        <div class="day-meta">
          <span><i class="fa-solid fa-location-dot"></i> ${d.location}</span>
          <span><i class="fa-solid fa-car"></i> ${d.distance}</span>
        </div>
      </div>

      <div class="info-block">
        <div class="info-block-title">
          <i class="fa-solid fa-hotel" style="color: #2563eb;"></i>
          <span>Accommodation: ${d.hotel}</span>
          <span class="badge-tag ${statusCls}">${statusLabel}</span>
        </div>
        <div style="font-size: 0.85rem; color: #475569; margin-left: 24px;">
          <strong>Booking Reference:</strong> ${d.bookingRef}
        </div>
      </div>

      <div style="margin-bottom: 12px; color: #334155; font-size: 0.95rem;">
        <strong><i class="fa-solid fa-compass" style="color: #2563eb; margin-right: 6px;"></i>Key Activities & Sights:</strong><br/>
        ${d.activities}
      </div>

      <div style="font-size: 0.88rem; color: #64748b; background: #f1f5f9; padding: 10px 14px; border-radius: 6px; margin-top: 10px;">
        <strong><i class="fa-solid fa-clipboard-list" style="margin-right: 6px;"></i>Logistics & Notes:</strong> ${d.scheduleNotes}
      </div>

      <div class="tag-list">
        ${tagsHtml}
      </div>
    `;
    container.appendChild(card);
  });
}
