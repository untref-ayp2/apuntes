(function () {
    /**
     * Este código se encarga de recordar el estado del sidebar (oculto o visible)
     * entre recargas de página, utilizando localStorage.
     * Adaptado para MyST (jupyter-book v2)
     */
    document.addEventListener("DOMContentLoaded", function onDOMContentLoaded() {
        const hideSidebarKey = "hide-sidebar";
        const hideSidebarValue = localStorage.getItem(hideSidebarKey);
        const hideSidebar = hideSidebarValue ? JSON.parse(hideSidebarValue) : false;

        // MyST usa "sidebar-toggle" para el checkbox
        const hideSidebarCheckbox = document.getElementById(
            "sidebar-toggle"
        );

        if (hideSidebarCheckbox) {
            hideSidebarCheckbox.checked = hideSidebar;

            document
                .querySelector(".sidebar-toggle")
                .addEventListener("click", function () {
                    setTimeout(function () {
                        localStorage.setItem(
                            hideSidebarKey,
                            JSON.stringify(hideSidebarCheckbox.checked)
                        );
                    }, 0);
                });
        }
    });
})();
