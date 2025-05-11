;
    function toggleMenu() {
      document.querySelector('.sidebar').classList.toggle('active');
    }

    function showSection(sectionId) {
      document.querySelectorAll('.section').forEach(sec => sec.classList.remove('active'));
      document.getElementById(sectionId).classList.add('active');
      document.querySelectorAll('.sidebar ul li').forEach(li => li.classList.remove('active'));
      const index = ['report','illegal','profile','notifications','mapSection'].indexOf(sectionId);
      document.querySelectorAll('.sidebar ul li')[index].classList.add('active');
      document.querySelector('.sidebar').classList.remove('active'); // collapse on mobile
    }

    function showSubTypes() {
      const type = document.getElementById('wasteType').value;
      let html = '';
      if (type === 'organic') {
        const items = ['Pig Feed Waste(Fruit & veggie scraps, rice, stale bread, eggshells)', 'Compostable Waste(Tea leaves, coffee grounds, garden waste, spoiled fruits/veggies)'];
        html += items.map(item => `
          <label><input type="checkbox" onchange="toggleQty(this)">${item}</label>
          <input type="number" placeholder="Quantity (kg)" disabled class="qty-input">
        `).join('<br>');
      } else if (type === 'nonorganic') {
        const items = ['Plastic Bottle', 'Glass Bottle', 'Metal Scrap', 'Copy Books'];
        html += items.map(item => `
          <label><input type="checkbox" onchange="toggleQty(this)">${item}</label>
          <input type="number" placeholder="Quantity (kg)" disabled class="qty-input">
        `).join('<br>');
      } else if (type === 'ewaste') {
        const items = ['Small (phones)', 'Medium (printers)', 'Large (TVs)'];
        html += items.map(item => `
          <label><input type="checkbox" onchange="toggleQty(this)">${item}</label>
          <input type="number" placeholder="Quantity" disabled class="qty-input">
        `).join('<br>');
      }
      document.getElementById('subTypes').innerHTML = html;
    }

    function toggleQty(checkbox) {
      const input = checkbox.parentElement.nextElementSibling;
      input.disabled = !checkbox.checked;
    }

    // MAP INIT (OPTIONAL)
    document.addEventListener("DOMContentLoaded", () => {
      if (document.getElementById("map")) {
        const map = L.map('map').setView([27.7172, 85.3240], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19
        }).addTo(map);
      }
    });
 