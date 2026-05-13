public class Persona {
    private String nombre;
    private String direccion;
    private String dni;

    public Persona(String nombre, String direccion, String dni) {
        this.nombre = nombre;
        this.direccion = direccion;
        this.dni = dni;
    }

    public String saludar() {
        return "¡Hola! Soy " + nombre;
    }

    public String caminar() {
        return nombre + " está caminando";
    }

    public String getNombre() {
        return nombre;
    }
}
