public class Estudiante extends Persona {
    private int legajo;

    public Estudiante(String nombre, String direccion, String dni, int legajo) {
        super(nombre, direccion, dni);
        this.legajo = legajo;
    }

    @Override
    public String saludar() {
        return "¡Hola! Soy " + getNombre() + " y soy estudiante (legajo: " + legajo + ")";
    }

    public String cursarMateria(String materia) {
        return getNombre() + " se inscribió en " + materia;
    }
}
