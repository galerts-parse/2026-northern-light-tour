// 2026 Northern Light Tour Application Script (Multi-Route & Google Maps Enabled)

let globalPayload = null;
let currentRouteKey = 'routeB'; // Default to Route B (High-Action Nature & Foodie)

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    initPasswordProtection();
  });
} else {
  initPasswordProtection();
}

function initPasswordProtection() {
  const authOverlay = document.getElementById('auth-overlay');
  const authModal = document.getElementById('auth-modal');
  const authForm = document.getElementById('auth-form');
  const pinInput = document.getElementById('pin-hidden-input');
  const boxes = document.querySelectorAll('.pin-digit-box');
  const authErrorMsg = document.getElementById('auth-error-msg');

  if (!authOverlay) return;

  const savedPin = sessionStorage.getItem('auth_pin');
  if (savedPin) {
    if (tryDecryptAndRender(savedPin)) {
      authOverlay.style.display = 'none';
      return;
    } else {
      sessionStorage.removeItem('auth_pin');
      sessionStorage.removeItem('auth_passed');
    }
  }

  if (pinInput) {
    setTimeout(() => {
      try { pinInput.focus(); } catch (e) {}
    }, 150);
  }

  function updateVisualBoxes() {
    if (!pinInput || !boxes.length) return;
    const val = pinInput.value.replace(/\D/g, '').slice(0, 4);
    pinInput.value = val;

    boxes.forEach((box, i) => {
      if (i < val.length) {
        box.textContent = '•';
        box.classList.add('filled');
        box.classList.remove('active');
      } else {
        box.textContent = '';
        box.classList.remove('filled');
        if (i === val.length) {
          box.classList.add('active');
        } else {
          box.classList.remove('active');
        }
      }
    });

    if (val.length === 4) {
      verifyPin();
    }
  }

  if (pinInput) {
    pinInput.addEventListener('input', updateVisualBoxes);
    pinInput.addEventListener('keyup', updateVisualBoxes);
  }

  if (authForm) {
    authForm.addEventListener('submit', (e) => {
      e.preventDefault();
      verifyPin();
    });
  }

  if (authModal) {
    authModal.addEventListener('click', () => {
      if (pinInput) pinInput.focus();
    });
  }

  function verifyPin() {
    if (!pinInput) return;
    const enteredPin = pinInput.value.trim();

    if (enteredPin.length < 4) return;

    if (tryDecryptAndRender(enteredPin)) {
      sessionStorage.setItem('auth_passed', 'true');
      sessionStorage.setItem('auth_pin', enteredPin);
      authOverlay.style.display = 'none';
      if (authErrorMsg) authErrorMsg.style.display = 'none';
    } else {
      if (authErrorMsg) authErrorMsg.style.display = 'block';
      if (authModal) {
        authModal.classList.add('shake');
        setTimeout(() => authModal.classList.remove('shake'), 500);
      }
      pinInput.value = '';
      updateVisualBoxes();
      try { pinInput.focus(); } catch (e) {}
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

      setupRouteSelector();
      renderCurrentRoute();
      return true;
    }
  } catch (e) {
    console.error('Decryption failed:', e);
  }
  return false;
}

function setupRouteSelector() {
  const routeSelect = document.getElementById('route-selector');
  if (routeSelect && globalPayload && globalPayload.routes) {
    routeSelect.innerHTML = '';
    Object.keys(globalPayload.routes).forEach(key => {
      const r = globalPayload.routes[key];
      const opt = document.createElement('option');
      opt.value = key;
      opt.textContent = r.name;
      if (key === currentRouteKey) opt.selected = true;
      routeSelect.appendChild(opt);
    });

    routeSelect.addEventListener('change', (e) => {
      currentRouteKey = e.target.value;
      renderCurrentRoute();
    });
  }
}

function renderCurrentRoute() {
  if (!globalPayload || !globalPayload.routes) return;
  const activeRoute = globalPayload.routes[currentRouteKey] || globalPayload.routes['routeB'];
  const itineraryData = activeRoute.days;

  if (document.getElementById('map')) {
    initItineraryMap(itineraryData);
  }
  if (document.getElementById('tour-package-content')) {
    renderTourPackageView(globalPayload, activeRoute);
  }
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
        <a href="${day.gmaps}" target="_blank" style="display:inline-block; margin-top:8px; background:#ea580c; color:white; padding:4px 8px; border-radius:4px; text-decoration:none; font-size:11px; font-weight:bold;"><i class="fa-solid fa-location-arrow"></i> Google Maps GPS</a>
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
function renderTourPackageView(payload, activeRoute) {
  const container = document.getElementById('tour-package-content');
  const navContainer = document.getElementById('sidebar-nav-ul');
  if (!container || !activeRoute) return;

  const itineraryData = activeRoute.days;

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

    // Hourly schedule with Google Maps links
    const hourlyHtml = (d.hourlySchedule || []).map(h => `
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px; font-size: 0.88rem; border-bottom: 1px dashed #e2e8f0; padding-bottom: 4px;">
        <div>
          <span style="font-weight: 700; color: #2563eb; width: 100px; display: inline-block;">${h.time}</span>
          <span style="color: #334155;">${h.activity}</span>
        </div>
        ${h.gmaps ? `<a href="${h.gmaps}" target="_blank" class="action-btn orange" style="font-size: 10px; padding: 2px 6px; flex-shrink: 0;"><i class="fa-solid fa-location-arrow"></i> GPS</a>` : ''}
      </div>
    `).join('');

    // Food Guide (Good vs Cheap)
    let foodHtml = '';
    if (d.foodGuide) {
      const fg = d.foodGuide;
      foodHtml = `
        <div class="info-block" style="background: #fff7ed; border: 1px solid #fed7aa;">
          <div class="info-block-title" style="color: #c2410c;"><i class="fa-solid fa-utensils"></i> Recommended City Food Guide (Good vs Local Cheap Eats):</div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 10px; margin-top: 6px;">
            <div style="background: white; padding: 10px; border-radius: 6px; border: 1px solid #ffedd5;">
              <span style="font-weight: 700; color: #ea580c; font-size: 12px;">★ Top Regional Dining:</span><br/>
              <strong style="font-size: 13px; color: #1e293b;">${fg.good.name}</strong> (${fg.good.cost})<br/>
              <span style="font-size: 11px; color: #64748b;">${fg.good.desc}</span><br/>
              <a href="${fg.good.gmaps}" target="_blank" class="action-btn orange" style="font-size: 10px; padding: 2px 6px; margin-top: 4px; display: inline-flex;"><i class="fa-solid fa-location-arrow"></i> Google Maps GPS</a>
            </div>
            <div style="background: white; padding: 10px; border-radius: 6px; border: 1px solid #ffedd5;">
              <span style="font-weight: 700; color: #16a34a; font-size: 12px;">★ Local Cheap Eats / Market:</span><br/>
              <strong style="font-size: 13px; color: #1e293b;">${fg.cheap.name}</strong> (${fg.cheap.cost})<br/>
              <span style="font-size: 11px; color: #64748b;">${fg.cheap.desc}</span><br/>
              <a href="${fg.cheap.gmaps}" target="_blank" class="action-btn green" style="font-size: 10px; padding: 2px 6px; margin-top: 4px; display: inline-flex;"><i class="fa-solid fa-location-arrow"></i> Google Maps GPS</a>
            </div>
          </div>
        </div>
      `;
    }

    // Hotel links & Maps
    const hotelLinksHtml = (d.hotelLinks || []).map(hl => `
      <a href="${hl.url}" target="_blank" class="action-btn blue" style="font-size: 11px; padding: 3px 8px; margin-right: 4px;"><i class="fa-solid fa-arrow-up-right-from-square"></i> Book ${hl.name}</a>
      ${hl.gmaps ? `<a href="${hl.gmaps}" target="_blank" class="action-btn orange" style="font-size: 11px; padding: 3px 8px;"><i class="fa-solid fa-location-arrow"></i> Hotel GPS</a>` : ''}
    `).join(' ');

    // Tickets & Costs
    const ticketsHtml = (d.ticketCosts || []).map(t => `
      <div style="display: flex; justify-content: space-between; align-items: center; background: white; padding: 8px 12px; border-radius: 6px; margin-bottom: 6px; font-size: 0.85rem; border: 1px solid #e2e8f0;">
        <span><strong>${t.item}</strong> (${t.cost})</span>
        <a href="${t.url}" target="_blank" class="action-btn green" style="font-size: 11px; padding: 3px 8px;"><i class="fa-solid fa-ticket"></i> Buy Ticket</a>
      </div>
    `).join('');

    // Aurora Spots with GPS
    const auroraHtml = (d.auroraSpots || []).map(a => `
      <div style="background: #0f172a; color: #f8fafc; padding: 10px 14px; border-radius: 8px; margin-top: 10px; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
        <div>
          <span style="color: #38bdf8; font-weight: 700;"><i class="fa-solid fa-meteor"></i> Self-Drive Aurora Spot: ${a.name}</span><br/>
          <span style="color: #cbd5e1;">${a.desc}</span>
        </div>
        <a href="${a.gmaps}" target="_blank" class="action-btn orange" style="font-size: 11px; padding: 4px 8px; flex-shrink: 0;"><i class="fa-solid fa-location-arrow"></i> Aurora GPS</a>
      </div>
    `).join('');

    // Outdoor Trails & Terrain Details
    const trailsHtml = (d.trails || []).map(tr => `
      <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px; border-radius: 8px; margin-top: 10px;">
        <div style="font-weight: 700; color: #15803d; font-size: 0.9rem; display: flex; justify-content: space-between; align-items: center;">
          <span><i class="fa-solid fa-person-hiking"></i> Outdoor Trail: ${tr.name}</span>
          ${tr.parkUrl ? `<a href="${tr.parkUrl}" target="_blank" class="action-btn green" style="font-size: 10px; padding: 2px 6px;"><i class="fa-solid fa-tree"></i> ${tr.parkName || 'Park Site'}</a>` : ''}
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 8px; margin-top: 8px; font-size: 0.82rem; color: #334155;">
          <div><strong>Walk Distance:</strong> ${tr.distance}</div>
          <div><strong>Duration:</strong> ${tr.duration}</div>
          ${tr.elevation ? `<div><strong>Elevation Profile:</strong> ${tr.elevation}</div>` : ''}
        </div>
        <div style="margin-top: 6px; font-size: 0.82rem; color: #475569; border-top: 1px dashed #cbd5e1; padding-top: 6px;">
          <strong>Terrain & Gear:</strong> ${tr.terrain}
        </div>
        ${tr.trailheadGmaps ? `<a href="${tr.trailheadGmaps}" target="_blank" class="action-btn orange" style="font-size: 10px; padding: 2px 6px; margin-top: 6px; display: inline-flex;"><i class="fa-solid fa-location-arrow"></i> Trailhead / Parking GPS</a>` : ''}
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
          <a href="${d.gmaps}" target="_blank" class="action-btn orange" style="font-size: 11px; padding: 3px 8px;"><i class="fa-solid fa-location-arrow"></i> Day GPS</a>
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

      ${trailsHtml}

      ${foodHtml}

      ${ticketsHtml ? `
        <div class="info-block" style="background: #f0fdf4;">
          <div class="info-block-title"><i class="fa-solid fa-ticket" style="color: #16a34a;"></i> Required Tickets & Booking Links:</div>
          ${ticketsHtml}
        </div>
      ` : ''}

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
          <div style="background: #fef2f2; padding: 12px; border-radius: 8px; border: 1px solid #fecaca; display: flex; justify-content: space-between; align-items: center;">
            <div>
              <div style="font-weight: 700; color: #991b1b; font-size: 14px;">${c.country}: ${c.number}</div>
              <div style="font-size: 12px; color: #7f1d1d;">${c.desc}</div>
            </div>
            ${c.gmaps ? `<a href="${c.gmaps}" target="_blank" class="action-btn orange" style="font-size: 10px; padding: 2px 6px;"><i class="fa-solid fa-location-arrow"></i> GPS</a>` : ''}
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
