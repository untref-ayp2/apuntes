package persona

import "fmt"

type Estudiante struct {
	Persona
	legajo int
}

func NewEstudiante(nombre, direccion, dni string, legajo int) (*Estudiante, error) {
	if legajo <= 0 {
		return nil, fmt.Errorf("el legajo debe ser positivo, se recibió: %d", legajo)
	}
	p, err := NewPersona(nombre, direccion, dni)
	if err != nil {
		return nil, err
	}
	return &Estudiante{Persona: *p, legajo: legajo}, nil
}

func (e Estudiante) Saludar() string {
	return fmt.Sprintf("¡Hola! Soy %s y soy estudiante (legajo: %d)", e.nombre, e.legajo)
}

func (e Estudiante) CursarMateria(materia string) string {
	return fmt.Sprintf("%s se inscribió en %s", e.nombre, materia)
}
