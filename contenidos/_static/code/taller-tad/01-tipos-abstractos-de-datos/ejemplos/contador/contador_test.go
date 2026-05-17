package contador

import "testing"

func TestNuevoContador(t *testing.T) {
	c, err := NuevoContador(0, 10)
	if err != nil {
		t.Fatalf("error inesperado: %v", err)
	}
	if c.Valor() != 0 {
		t.Errorf("valor inicial esperado 0, got %d", c.Valor())
	}
	if c.Cambios() != 0 {
		t.Errorf("cambios inicial esperado 0, got %d", c.Cambios())
	}
}

func TestIncrementar(t *testing.T) {
	c, _ := NuevoContador(0, 10)
	err := c.Incrementar()
	if err != nil {
		t.Fatalf("error inesperado: %v", err)
	}
	if c.Valor() != 1 {
		t.Errorf("valor esperado 1, got %d", c.Valor())
	}
	if c.Cambios() != 1 {
		t.Errorf("cambios esperado 1, got %d", c.Cambios())
	}
}

func TestIncrementarLimite(t *testing.T) {
	c, _ := NuevoContador(0, 1)
	c.Incrementar()
	err := c.Incrementar()
	if err == nil {
		t.Error("se esperaba error al superar el máximo")
	}
}

func TestDecrementar(t *testing.T) {
	c, _ := NuevoContador(0, 10)
	c.Incrementar()
	err := c.Decrementar()
	if err != nil {
		t.Fatalf("error inesperado: %v", err)
	}
	if c.Valor() != 0 {
		t.Errorf("valor esperado 0, got %d", c.Valor())
	}
}

func TestDecrementarLimite(t *testing.T) {
	c, _ := NuevoContador(0, 10)
	err := c.Decrementar()
	if err == nil {
		t.Error("se esperaba error al superar el mínimo")
	}
}

func TestConstructorInvalido(t *testing.T) {
	_, err := NuevoContador(10, 0)
	if err == nil {
		t.Error("se esperaba error con min > max")
	}
}
