// 2026 Northern Light Tour Application Script

document.addEventListener('DOMContentLoaded', () => {
  initPasswordProtection();
  initItineraryApp();
});

// Password Protection Logic (PIN: 8520)
function initPasswordProtection() {
  const authOverlay = document.getElementById('auth-overlay');
  const authModal = document.getElementById('auth-modal');
  const authSubmitBtn = document.getElementById('auth-submit-btn');
  const authErrorMsg = document.getElementById('auth-error-msg');
  const pinInputs = document.querySelectorAll('.pin-digit');

  if (!authOverlay) return;

  // Check existing session
  if (sessionStorage.getItem('auth_passed') === 'true') {
    authOverlay.style.display = 'none';
    return;
  }

  // Focus first digit
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

    if (enteredPin === '8520') {
      sessionStorage.setItem('auth_passed', 'true');
      authOverlay.style.display = 'none';
    } else {
      authErrorMsg.style.display = 'block';
      authModal.classList.add('shake');
      setTimeout(() => authModal.classList.remove('shake'), 500);
      pinInputs.forEach(i => i.value = '');
      pinInputs[0].focus();
    }
  }
}

// Map & Itinerary Application Logic
function initItineraryApp() {
  const mapElem = document.getElementById('map');
  const listElem = document.getElementById('itinerary-list');

  if (!mapElem || typeof L === 'undefined' || typeof itineraryData === 'undefined') return;

  // Initialize Leaflet Map centered on Lapland/Nordics
  const map = L.map('map').setView([65.8252, 23.6886], 5);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  const markers = [];
  const latLngs = [];

  // Render Sidebar and Markers
  itineraryData.forEach((day, index) => {
    latLngs.push(day.coords);

    // Custom marker icon color depending on hotel status
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

  // Polyline for Route
  const polyline = L.polyline(latLngs, {
    color: '#2563eb',
    weight: 4,
    opacity: 0.8,
    dashArray: '8, 8'
  }).addTo(map);

  map.fitBounds(polyline.getBounds(), { padding: [40, 40] });
}
