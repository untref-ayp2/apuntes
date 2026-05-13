package persona

import "fmt"

type PersonaInterface interface {
	Saludar() string
	Caminar() string
}

type Persona struct {
	nombre    string
	direccion string
	dni       string
}

func NewPersona(nombre, direccion, dni string) (*Persona, error) {
	if dni == "" {
		return nil, fmt.Errorf("el DNI no puede estar vacío")
	}
	return &Persona{nombre: nombre, direccion: direccion, dni: dni}, nil
}

func (p Persona) Saludar() string {
	return fmt.Sprintf("¡Hola! Soy %s", p.nombre)
}

func (p Persona) Caminar() string {
	return fmt.Sprintf("%s está caminando", p.nombre)
}
