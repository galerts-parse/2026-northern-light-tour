// 2026 Northern Light Tour Application Script (AES Decrypted Engine)

let globalPayload = null;

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

  if (pinInputs.length > 0) {
    pinInputs[0].focus();
  }

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
    
    if (decryptedText && decryptedText.trim().startsWith('{')) {
      globalPayload = JSON.parse(decryptedText);
      const itineraryData = globalPayload.days;

      if (document.getElementById('map')) {
        initItineraryMap(itineraryData);
      }
      if (document.getElementById('tour-package-content')) {
        renderTourPackageView(globalPayload);
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

  if (listElem) listElem.innerHTML = '';

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

// Render Tour Package View for tour_package.html
function renderTourPackageView(payload) {
  const container = document.getElementById('tour-package-content');
  const navContainer = document.getElementById('sidebar-nav-ul');
  if (!container || !payload) return;

  const itineraryData = payload.days;

  container.innerHTML = '';
  if (navContainer) navContainer.innerHTML = '';

  // 1. Sidebar Nav
  if (navContainer) {
    itineraryData.forEach(d => {
      const li = document.createElement('li');
      li.innerHTML = `<a href="#day-${d.day}">Day ${d.day}: ${d.location.split(',')[0]}</a>`;
      navContainer.appendChild(li);
    });
    const extraLi1 = document.createElement('li');
    extraLi1.innerHTML = `<a href="#emergency-section" style="color: #dc2626; font-weight:600;"><i class="fa-solid fa-triangle-exclamation"></i> Emergency & Safety</a>`;
    navContainer.appendChild(extraLi1);
    const extraLi2 = document.createElement('li');
    extraLi2.innerHTML = `<a href="#packing-section" style="color: #16a34a; font-weight:600;"><i class="fa-solid fa-suitcase"></i> Packing Checklist</a>`;
    navContainer.appendChild(extraLi2);
  }

  // 2. Day Cards
  itineraryData.forEach((d) => {
    const statusCls = d.hotelStatus;
    const statusLabel = statusCls === 'confirmed' ? '✅ Confirmed' : '📌 Booking Pending';
    const tagsHtml = (d.tags || []).map(t => `<span class="chip">#${t}</span>`).join('');

    // Hourly schedule
    const hourlyHtml = (d.hourlySchedule || []).map(h => `
      <div style="display: flex; gap: 12px; margin-bottom: 8px; font-size: 0.88rem;">
        <span style="font-weight: 700; color: #2563eb; width: 100px; flex-shrink: 0;">${h.time}</span>
        <span style="color: #334155;">${h.activity}</span>
      </div>
    `).join('');

    // Hotel links
    const hotelLinksHtml = (d.hotelLinks || []).map(hl => `
      <a href="${hl.url}" target="_blank" class="action-btn blue" style="font-size: 11px; padding: 4px 8px; margin-top: 4px; display: inline-flex;"><i class="fa-solid fa-arrow-up-right-from-square"></i> Book ${hl.name}</a>
    `).join(' ');

    // Tickets & Costs
    const ticketsHtml = (d.ticketCosts || []).map(t => `
      <div style="display: flex; justify-content: space-between; align-items: center; background: white; padding: 8px 12px; border-radius: 6px; margin-bottom: 6px; font-size: 0.85rem; border: 1px solid #e2e8f0;">
        <span><strong>${t.item}</strong> (${t.cost})</span>
        <a href="${t.url}" target="_blank" class="action-btn green" style="font-size: 11px; padding: 3px 8px;"><i class="fa-solid fa-ticket"></i> Buy Ticket</a>
      </div>
    `).join('');

    // Operator Comparisons
    const opsHtml = (d.operatorComparisons || []).map(o => `
      <div style="background: #fff7ed; border-left: 3px solid #ea580c; padding: 10px; border-radius: 6px; margin-top: 8px; font-size: 0.85rem;">
        <strong><i class="fa-solid fa-code-compare"></i> ${o.activity} Operator Comparison:</strong><br/>
        &bull; <strong>Option 1:</strong> ${o.op1}<br/>
        &bull; <strong>Option 2:</strong> ${o.op2}<br/>
        <span style="color: #16a34a; font-weight: 700;">★ Recommended: ${o.rec}</span>
      </div>
    `).join('');

    // Aurora Spots
    const auroraHtml = (d.auroraSpots || []).map(a => `
      <div style="background: #0f172a; color: #f8fafc; padding: 10px 14px; border-radius: 8px; margin-top: 10px; font-size: 0.85rem;">
        <span style="color: #38bdf8; font-weight: 700;"><i class="fa-solid fa-meteor"></i> Self-Drive Aurora Spot: ${a.name}</span><br/>
        <span style="color: #cbd5e1;">${a.desc}</span>
      </div>
    `).join('');

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
        <div style="font-size: 0.85rem; color: #475569; margin-left: 24px; margin-bottom: 6px;">
          <strong>Booking Ref / Status:</strong> ${d.bookingRef}
        </div>
        ${hotelLinksHtml ? `<div style="margin-left: 24px;">${hotelLinksHtml}</div>` : ''}
      </div>

      <div style="margin-bottom: 15px; color: #334155; font-size: 0.95rem;">
        <strong><i class="fa-solid fa-compass" style="color: #2563eb; margin-right: 6px;"></i>Key Highlights:</strong><br/>
        ${d.activities}
      </div>

      <div class="info-block" style="background: #f8fafc;">
        <div class="info-block-title"><i class="fa-solid fa-clock" style="color: #2563eb;"></i> Hourly Schedule Breakdown:</div>
        ${hourlyHtml}
      </div>

      ${ticketsHtml ? `
        <div class="info-block" style="background: #f0fdf4;">
          <div class="info-block-title"><i class="fa-solid fa-ticket" style="color: #16a34a;"></i> Required Tickets & Booking Links:</div>
          ${ticketsHtml}
        </div>
      ` : ''}

      ${opsHtml}
      ${auroraHtml}

      <div class="tag-list" style="margin-top: 15px;">
        ${tagsHtml}
      </div>
    `;
    container.appendChild(card);
  });

  // 3. Emergency & Safety Section
  if (payload.emergencyGuide) {
    const eg = payload.emergencyGuide;
    const emergencyCard = document.createElement('div');
    emergencyCard.id = 'emergency-section';
    emergencyCard.className = 'day-card';
    emergencyCard.style.borderLeft = '4px solid #dc2626';
    emergencyCard.innerHTML = `
      <h2 style="margin-top:0; color: #dc2626;"><i class="fa-solid fa-shield-halved"></i> Emergency Contacts & Winter Driving Unstuck Guide</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 20px;">
        ${eg.contacts.map(c => `
          <div style="background: #fef2f2; padding: 12px; border-radius: 8px; border: 1px solid #fecaca;">
            <div style="font-weight: 700; color: #991b1b; font-size: 14px;">${c.country}: ${c.number}</div>
            <div style="font-size: 12px; color: #7f1d1d;">${c.desc}</div>
          </div>
        `).join('')}
      </div>

      <div class="info-block" style="background: #fffbeb; border: 1px solid #fde68a;">
        <div class="info-block-title" style="color: #b45309;"><i class="fa-solid fa-snowflake"></i> How to Get Unstuck in Deep Snow (6 Steps):</div>
        <ol style="margin: 0; padding-left: 20px; font-size: 0.88rem; color: #78350f;">
          ${eg.unstuckSteps.map(s => `<li style="margin-bottom: 6px;">${s}</li>`).join('')}
        </ol>
      </div>

      <div class="info-block" style="background: #f8fafc;">
        <div class="info-block-title"><i class="fa-solid fa-triangle-exclamation"></i> Winter Driving Do's & Don'ts:</div>
        <ul style="margin: 0; padding-left: 20px; font-size: 0.88rem; color: #334155;">
          ${eg.dosAndDonts.map(d => `<li style="margin-bottom: 4px;">${d}</li>`).join('')}
        </ul>
      </div>
    `;
    container.appendChild(emergencyCard);
  }

  // 4. Packing Checklist Section
  if (payload.packingChecklist) {
    const packingCard = document.createElement('div');
    packingCard.id = 'packing-section';
    packingCard.className = 'day-card';
    packingCard.style.borderLeft = '4px solid #16a34a';
    packingCard.innerHTML = `
      <h2 style="margin-top:0; color: #16a34a;"><i class="fa-solid fa-suitcase"></i> Comprehensive Arctic Packing Checklist</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
        ${payload.packingChecklist.map(cat => `
          <div style="background: #f0fdf4; padding: 15px; border-radius: 10px; border: 1px solid #bbf7d0;">
            <h4 style="margin: 0 0 10px 0; color: #15803d;"><i class="fa-solid fa-check-double"></i> ${cat.cat}</h4>
            <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.85rem; color: #166534;">
              ${cat.items.map(item => `
                <li style="margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
                  <input type="checkbox" style="cursor: pointer;">
                  <span>${item}</span>
                </li>
              `).join('')}
            </ul>
          </div>
        `).join('')}
      </div>
    `;
    container.appendChild(packingCard);
  }
}
