#!/bin/bash
# Script para crear versiones light/dark de SVGs vectoriales

cd /home/martin/AyP2/apuntes/contenidos/_static/figures

# Colores para light
LIGHT_BG="#ffffff"
LIGHT_TEXT="#333333"
LIGHT_STROKE="#333333"

# Colores para dark  
DARK_BG="#1e1e1e"
DARK_TEXT="#e0e0e0"
DARK_STROKE="#e0e0e0"

process_svg() {
    local input=$1
    local output_light="${input%.svg}_light.svg"
    local output_dark="${input%.svg}_dark.svg"
    
    # Crear versión light
    sed -e "s/#ffffff/$LIGHT_BG/g" \
        -e "s/#000000/$LIGHT_STROKE/g" \
        -e "s/#333333/$LIGHT_TEXT/g" \
        -e "s/<rect /<rect fill=\"$LIGHT_BG\" /g" \
        "$input" > "$output_light"
    
    # Crear versión dark
    sed -e "s/#ffffff/$DARK_BG/g" \
        -e "s/#000000/$DARK_STROKE/g" \
        -e "s/#333333/$DARK_TEXT/g" \
        -e "s/<rect /<rect fill=\"$DARK_BG\" /g" \
        "$input" > "$output_dark"
    
    echo "Creado: $output_light y $output_dark"
}

# Solo procesar SVGs que tienen contenido vectorial (contienen rect o path)
for svg in *.svg; do
    if grep -q "<rect \|<path " "$svg" 2>/dev/null; then
        if [[ ! "$svg" =~ (_light|_dark)\.svg$ ]]; then
            process_svg "$svg"
        fi
    fi
done

echo "Listo!"
