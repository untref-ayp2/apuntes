package contador

import "errors"

type Contador struct {
	actual  int
	minimo  int
	maximo  int
	cambios int
}

func NuevoContador(min, max int) (*Contador, error) {
	if min > max {
		return nil, errors.New("minimo no puede ser mayor que maximo")
	}
	return &Contador{
		actual:  min,
		minimo:  min,
		maximo:  max,
		cambios: 0,
	}, nil
}

func (c *Contador) Incrementar() error {
	if c.actual >= c.maximo {
		return errors.New("el contador ya alcanzó el máximo")
	}
	c.actual++
	c.cambios++
	return nil
}

func (c *Contador) Decrementar() error {
	if c.actual <= c.minimo {
		return errors.New("el contador ya alcanzó el mínimo")
	}
	c.actual--
	c.cambios++
	return nil
}

func (c *Contador) Valor() int {
	return c.actual
}

func (c *Contador) Cambios() int {
	return c.cambios
}
