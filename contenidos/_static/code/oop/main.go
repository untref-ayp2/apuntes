package main

import (
	"fmt"

	"apunte/oop/persona"
)

func main() {
	marcelo, err := persona.NewPersona("Marcelo", "Av. Siempre Viva 123", "12345678")
	if err != nil {
		fmt.Println(err)
		return
	}

	laura, err := persona.NewEstudiante("Laura", "Calle Falsa 456", "87654321", 2025001)
	if err != nil {
		fmt.Println(err)
		return
	}

	personas := []persona.PersonaInterface{marcelo, laura}

	for _, p := range personas {
		fmt.Println(p.Saludar())
		fmt.Println(p.Caminar())

		if e, ok := p.(*persona.Estudiante); ok {
			fmt.Println(e.CursarMateria("Algoritmos II"))
		}

		fmt.Println()
	}
}
