(() => {
  "use strict";

  const filters = document.querySelectorAll("[data-filter-table]");

  filters.forEach((input) => {
    const table = document.getElementById(input.dataset.filterTable);
    if (!table) return;

    const rows = Array.from(table.querySelectorAll("tbody tr"));
    const count = document.querySelector(`[data-filter-count="${input.dataset.filterTable}"]`);

    const update = () => {
      const query = input.value.trim().toLocaleLowerCase();
      let visible = 0;

      rows.forEach((row) => {
        const matches = !query || row.textContent.toLocaleLowerCase().includes(query);
        row.hidden = !matches;
        if (matches) visible += 1;
      });

      if (count) {
        count.textContent = query
          ? `${visible} of ${rows.length} entries`
          : `${rows.length} entries`;
      }
    };

    input.addEventListener("input", update);
    update();
  });
})();
