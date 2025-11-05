(function () {
    /**
     * Este código se encarga de recordar el estado del sidebar (oculto o visible)
     * entre recargas de página, utilizando localStorage.
     */
    document.addEventListener("DOMContentLoaded", function onDOMContentLoaded() {
        const hideSidebarKey = "hide-sidebar";
        const hideSidebarValue = localStorage.getItem(hideSidebarKey);
        const hideSidebar = hideSidebarValue ? JSON.parse(hideSidebarValue) : false;
        const hideSidebarCheckbox = document.getElementById(
            "pst-primary-sidebar-checkbox"
        );

        hideSidebarCheckbox.checked = hideSidebar;

        document
            .querySelector(".primary-toggle")
            .addEventListener("click", function () {
                setTimeout(function () {
                    localStorage.setItem(
                        hideSidebarKey,
                        JSON.stringify(hideSidebarCheckbox.checked)
                    );
                }, 0);
            });
    });
})();
