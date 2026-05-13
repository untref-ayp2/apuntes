public class Main {
    public static void main(String[] args) {
        Persona[] personas = new Persona[2];
        personas[0] = new Persona("Marcelo", "Av. Siempre Viva 123", "12345678");
        personas[1] = new Estudiante("Laura", "Calle Falsa 456", "87654321", 2025001);

        for (Persona p : personas) {
            System.out.println(p.saludar());
            System.out.println(p.caminar());

            if (p instanceof Estudiante) {
                System.out.println(((Estudiante) p).cursarMateria("Algoritmos II"));
            }

            System.out.println();
        }
    }
}
