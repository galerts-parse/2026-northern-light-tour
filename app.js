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

  // Helper: Detailed Booking & Confirmation Card Generator
  const getBookingInfoHtml = (dayNum, d) => {
    let accDetails = '';
    let transportDetails = '';

    // 1. Rental Car details for Days 1-14
    if (dayNum >= 1 && dayNum <= 14) {
      const carStatus = dayNum === 1 ? 'Pick-up @ RVN Airport (5:00 PM)' : (dayNum === 14 ? 'Drop-off @ RVN Airport (8:30 PM)' : 'In Use / Driving');
      transportDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 8px;">
          <div style="font-weight: 700; color: #0369a1; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-car"></i> Car Rental: Enterprise Rent-A-Car</span>
            <span style="background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight:700;">Ref: 2130932940</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Confirmation #:</strong> <code style="background: #f1f5f9; padding: 1px 5px; border-radius: 3px; font-weight:700; color: #0284c7;">2130932940</code></div>
            <div><strong>Renter:</strong> NIM YING NGAN (Enterprise Plus SKDG4SJ)</div>
            <div><strong>Vehicle Class:</strong> VW Golf or Similar (Automatic)</div>
            <div><strong>Daily Status:</strong> ${carStatus}</div>
            <div><strong>Pick-up:</strong> Rovaniemi Airport (Sat Dec 12 @ 5:00 PM)</div>
            <div><strong>Return:</strong> Rovaniemi Airport (Fri Dec 25 @ 8:30 PM)</div>
            <div><strong>Total Paid:</strong> $2,561.69 USD (€2,193.60 EUR)</div>
            <div><strong>Inclusions:</strong> Unlimited km, Zero Excess, CDW, RAP</div>
          </div>
        </div>
      `;
    }

    // 2. Specific accommodation details per day based on folder PDF bookings
    if (dayNum === 1) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #d97706; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-hotel"></i> Accommodation: ${d.hotel}</span>
            <span class="badge-tag pending">📌 Booking Recommended</span>
          </div>
          <div style="font-size: 0.82rem; color: #475569; margin-top: 4px;">
            <strong>Status:</strong> Unconfirmed in folder — Recommended stay in Rovaniemi after evening flight arrival (5:00 PM car pickup).
          </div>
        </div>
      `;
    } else if (dayNum === 2 || dayNum === 3) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-house-chimney"></i> Stuga i Storklinten (Boden, Sweden)</span>
            <span class="badge-tag confirmed">✅ Confirmed</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Booking Platform:</strong> Booking.com</div>
            <div><strong>Stay Duration:</strong> 2 Nights (Check-in Dec 13, Check-out Dec 15)</div>
            <div><strong>Check-in Window:</strong> Sun, Dec 13 (00:00 – 23:59)</div>
            <div><strong>Check-out Time:</strong> Tue, Dec 15 (until 12:00)</div>
            <div><strong>Location:</strong> Storklinten Ski Resort, Boden, Sweden</div>
          </div>
        </div>
      `;
    } else if (dayNum === 4) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-house-chimney"></i> Northernlight Cabin (Kiruna, Sweden)</span>
            <span class="badge-tag confirmed">✅ Confirmed</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Booking Platform:</strong> Booking.com</div>
            <div><strong>Stay Duration:</strong> 1 Night (Dec 15 – Dec 16)</div>
            <div><strong>Check-in Window:</strong> Tue, Dec 15 (15:00 – 23:59)</div>
            <div><strong>Check-out Time:</strong> Wed, Dec 16 (until 12:00)</div>
            <div><strong>Location:</strong> Kiruna, Sweden</div>
          </div>
        </div>
      `;
    } else if (dayNum >= 5 && dayNum <= 7) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-building-user"></i> Aurora View Apt – Walk to Train & Ski (Kiruna V / Björkliden)</span>
            <span class="badge-tag confirmed">✅ Confirmed</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Airbnb Conf Code:</strong> <code style="background: #f1f5f9; padding: 1px 5px; border-radius: 3px; font-weight:700; color: #16a34a;">HM2B8KDQ4H</code></div>
            <div><strong>Host / Contact:</strong> Renberget (Co-hosts: Malin, Lena, Magnus, Daniel)</div>
            <div><strong>Address:</strong> GAMMELGÅRDSVÄGEN 10 Lgh, Kiruna V 981 93, Sweden</div>
            <div><strong>Check-in:</strong> Wed, Dec 16 @ 3:00 PM (Keypad Self Check-in)</div>
            <div><strong>Check-out:</strong> Sat, Dec 19 @ 12:00 PM</div>
            <div><strong>Total Paid:</strong> $748.92 SGD (3 Nights)</div>
          </div>
        </div>
      `;
    } else if (dayNum === 8 || dayNum === 9) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-building"></i> Cozy Apartment by the Sea 2 Rooms Free Private Parking (Kemi, Finland)</span>
            <span class="badge-tag confirmed">✅ Confirmed</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Booking Platform:</strong> Booking.com</div>
            <div><strong>Stay Duration:</strong> 2 Nights (Check-in Dec 19, Check-out Dec 21)</div>
            <div><strong>Check-in Window:</strong> Sat, Dec 19 (00:00 – 23:59)</div>
            <div><strong>Check-out Time:</strong> Mon, Dec 21 (11:00 – 12:00)</div>
            <div><strong>Location:</strong> Kemi, Lapland, Finland</div>
          </div>
        </div>
      `;
    } else if (dayNum === 10 || dayNum === 11) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-house-chimney-window"></i> Idyllic Sauna Cottage by the Lake (Posio, Finland)</span>
            <span class="badge-tag confirmed">✅ Confirmed</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Airbnb Conf Code:</strong> <code style="background: #f1f5f9; padding: 1px 5px; border-radius: 3px; font-weight:700; color: #16a34a;">HMYPAMHXW9</code></div>
            <div><strong>Host / Contact:</strong> Leena (Co-host: Tuomo)</div>
            <div><strong>Address:</strong> Rantapolku 1, Posio, Lappi 97900, Finland</div>
            <div><strong>Check-in:</strong> Mon, Dec 21 @ 3:00 PM (Lockbox Self Check-in)</div>
            <div><strong>Check-out:</strong> Wed, Dec 23 @ 11:00 AM</div>
            <div><strong>Total Paid:</strong> $379.67 SGD (2 Nights)</div>
          </div>
        </div>
      `;
    } else if (dayNum === 12) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-mountain-city"></i> Apartment with a View at top of Iso-Syöte (Pudasjärvi, Finland)</span>
            <span class="badge-tag confirmed">✅ Confirmed</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Airbnb Conf Code:</strong> <code style="background: #f1f5f9; padding: 1px 5px; border-radius: 3px; font-weight:700; color: #16a34a;">HMJ88QTC3C</code></div>
            <div><strong>Host / Contact:</strong> Arto</div>
            <div><strong>Address:</strong> Isosyötteentie 230 Näköalahuoneisto, Pudasjärvi 93280, Finland</div>
            <div><strong>Check-in:</strong> Wed, Dec 23 @ 3:00 PM</div>
            <div><strong>Check-out:</strong> Thu, Dec 24 @ 12:00 PM</div>
            <div><strong>Total Paid:</strong> $130.10 SGD (1 Night)</div>
          </div>
        </div>
      `;
    } else if (dayNum === 13) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-igloo"></i> Syöte Igloos / Iso-Syöte Glass Igloo</span>
            <span class="badge-tag confirmed">✅ Confirmed</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Booking Platform:</strong> Booking.com</div>
            <div><strong>Stay Duration:</strong> 1 Night (Dec 24 – Dec 25)</div>
            <div><strong>Check-in Window:</strong> Thu, Dec 24 (15:00 – 23:59)</div>
            <div><strong>Check-out Time:</strong> Fri, Dec 25 (06:00 – 12:00)</div>
            <div><strong>Location:</strong> Iso-Syöte, Pudasjärvi, Finland</div>
          </div>
        </div>
      `;
    } else if (dayNum === 14) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-train"></i> VR Santa Claus Express Overnight Sleeper Train 274</span>
            <span class="badge-tag confirmed">✅ Confirmed</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>VR Order No:</strong> <code style="background: #f1f5f9; padding: 1px 5px; border-radius: 3px; font-weight:700; color: #16a34a;">F3080273035361</code></div>
            <div><strong>Reference #:</strong> <code style="background: #f1f5f9; padding: 1px 5px; border-radius: 3px; font-weight:700; color: #16a34a;">2-PJ34-U4J7-UYEC</code></div>
            <div><strong>Train Route:</strong> Night Train 274 (Rovaniemi → Helsinki)</div>
            <div><strong>Departure:</strong> Fri, Dec 25 @ 21:00 (Rovaniemi Railway Station)</div>
            <div><strong>Arrival:</strong> Sat, Dec 26 @ 09:15 AM (Helsinki Central Station)</div>
            <div><strong>Cabin Type:</strong> 1 Accessible Sleeper Cabin for 2 people (€299.00 EUR Paid)</div>
          </div>
        </div>
      `;
    } else if (dayNum === 15) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #d97706; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-hotel"></i> Hotel U14, Autograph Collection (Helsinki)</span>
            <span class="badge-tag pending">📌 Booking Recommended</span>
          </div>
          <div style="font-size: 0.82rem; color: #475569; margin-top: 4px;">
            <strong>Recommendation:</strong> Modern Nordic boutique hotel 7 mins walk from Central Station. VR Train 274 arrives at 09:15 AM.
          </div>
        </div>
      `;
    } else if (dayNum === 16) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #d97706; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-hotel"></i> Hotel Telegraaf, Autograph Collection (Tallinn)</span>
            <span class="badge-tag pending">📌 Booking Recommended</span>
          </div>
          <div style="font-size: 0.82rem; color: #475569; margin-top: 4px;">
            <strong>Recommendation:</strong> Historic 1878 telegraph building located directly in Tallinn Old Town near Town Hall Square.
          </div>
        </div>
      `;
    } else if (dayNum === 17) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-ship"></i> Tallink Silja M/S Baltic Queen Overnight Baltic Cruise</span>
            <span class="badge-tag confirmed">✅ Confirmed Routing</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Vessel Name:</strong> M/S Baltic Queen (Tallink Silja Line)</div>
            <div><strong>Route:</strong> Tallinn D-Terminal → Stockholm Värtahamnen</div>
            <div><strong>Departure:</strong> Mon, Dec 28 @ 18:00 (Check-in 17:00)</div>
            <div><strong>Arrival:</strong> Tue, Dec 29 @ 10:30 AM (Stockholm Värtahamnen)</div>
            <div><strong>Cabin & Price:</strong> Private Sea-View Cabin (~€140 EUR / night)</div>
            <div><strong>Inclusions:</strong> Tax-free shopping, live shows, sauna & sea views</div>
          </div>
        </div>
      `;
    } else if (dayNum === 18 || dayNum === 19) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #d97706; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-hotel"></i> Sheraton Stockholm Hotel (Stockholm, Sweden)</span>
            <span class="badge-tag pending">📌 Booking Recommended</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Location:</strong> Tegelbacken 6 (3 mins walk to Central Station)</div>
            <div><strong>Stay Duration:</strong> 2 Nights (Check-in Tue Dec 29, Check-out Thu Dec 31)</div>
            <div><strong>Estimated Rate:</strong> ~1,900 SEK / ~$180 USD per night</div>
            <div><strong>Check-in Time:</strong> Tue, Dec 29 @ 15:00 (after 10:30 AM cruise arrival)</div>
          </div>
        </div>
      `;
    } else if (dayNum === 20 || dayNum === 21) {
      const sjRemark = dayNum === 20 ? `
        <div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 6px; padding: 8px; margin-top: 6px; font-size: 0.82rem; color: #92400e;">
          <strong>📌 BOOK LATER REMINDER:</strong> SJ High-Speed Train tickets for Dec 31 (Stockholm → Copenhagen) release ~90 days in advance in <strong>late September / early October 2026</strong>. Set an alert on <a href="https://www.sj.se/en" target="_blank" style="color: #b45309; font-weight:700;">SJ.se</a> or <a href="https://www.omio.com" target="_blank" style="color: #b45309; font-weight:700;">Omio.com</a>!
        </div>
      ` : '';

      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #d97706; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-hotel"></i> Copenhagen Marriott Hotel (Copenhagen, Denmark)</span>
            <span class="badge-tag pending">📌 Booking Recommended (NYE)</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Location:</strong> Kalvebod Brygge 5 (10 mins walk to Tivoli Gardens)</div>
            <div><strong>Stay Duration:</strong> 2 Nights (Check-in Thu Dec 31, Check-out Sat Jan 02)</div>
            <div><strong>Estimated Rate:</strong> ~2,100 DKK / ~$300 USD per night (NYE Peak)</div>
            <div><strong>Check-in Time:</strong> Thu, Dec 31 @ 15:00 (after 13:30 train arrival)</div>
          </div>
          ${sjRemark}
        </div>
      `;
    } else if (dayNum === 22) {
      accDetails = `
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; margin-top: 6px;">
          <div style="font-weight: 700; color: #15803d; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center;">
            <span><i class="fa-solid fa-plane"></i> Flight Home: Singapore Airlines SQ352 Non-stop</span>
            <span class="badge-tag confirmed">✅ Confirmed Flight</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 6px; margin-top: 6px; font-size: 0.82rem; color: #334155;">
            <div><strong>Flight Number:</strong> SQ352 (Non-stop)</div>
            <div><strong>Departure:</strong> CPH Terminal 3 @ Sat, Jan 02 @ 12:00 PM</div>
            <div><strong>Arrival:</strong> SIN Changi @ Sun, Jan 03 @ 07:30 AM</div>
          </div>
        </div>
      `;
    }

    const hotelLinksHtml = (d.hotelLinks || []).map(hl => `
      <a href="${hl.url}" target="_blank" class="action-btn blue" style="font-size: 11px; padding: 3px 8px; margin-right: 4px;"><i class="fa-solid fa-arrow-up-right-from-square"></i> Book ${hl.name}</a>
      ${hl.gmaps ? `<a href="${hl.gmaps}" target="_blank" class="action-btn orange" style="font-size: 11px; padding: 3px 8px;"><i class="fa-solid fa-location-arrow"></i> Hotel GPS</a>` : ''}
    `).join(' ');

    return `
      <div class="info-block" style="background: #f8fafc; border: 1px solid #cbd5e1; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-bottom: 15px;">
        <div class="info-block-title" style="color: #1e293b; font-size: 0.92rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 6px; display: flex; justify-content: space-between; align-items: center;">
          <span><i class="fa-solid fa-file-invoice" style="color: #2563eb;"></i> 📋 Reserved Booking Details & Confirmation References:</span>
          ${hotelLinksHtml ? `<div>${hotelLinksHtml}</div>` : ''}
        </div>
        ${accDetails}
        ${transportDetails}
      </div>
    `;
  };

  // 2. Day Cards
  itineraryData.forEach((d) => {
    const statusCls = d.hotelStatus;
    const statusLabel = statusCls === 'confirmed' ? '✅ Confirmed' : '📌 Booking Pending';
    const tagsHtml = (d.tags || []).map(t => `<span class="chip">#${t}</span>`).join('');
    const bookingBlockHtml = getBookingInfoHtml(d.day, d);

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

      ${bookingBlockHtml}

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
