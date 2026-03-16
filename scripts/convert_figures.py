#!/usr/bin/env python3
import re
import sys

def convert_figure(match):
    full_match = match.group(0)
    # Extraer la ruta de la imagen
    img_match = re.search(r'\.\./_static/figures/(\S+_light\.svg)', full_match)
    if img_match:
        img_name = img_match.group(1)
        base_name = img_name.replace('_light.svg', '')
        dark_name = f'{base_name}_dark.svg'
        
        # Extraer el título si existe
        title_match = re.search(r'\n([^#\n].+)\n?```$', full_match)
        title = title_match.group(1).strip() if title_match else base_name
        
        # Extraer options si existen
        options = ''
        if '---' in full_match:
            opts_match = re.search(r'---\n(.*?)\n---', full_match, re.DOTALL)
            if opts_match:
                options = opts_match.group(1)
                # Agregar class si no existe
                if 'class:' not in options:
                    options = options.rstrip() + '\nclass: only-light-mode\n'
        
        light_figure = "```{figure} ../_static/figures/" + img_name + "\n"
        if options:
            light_figure += "---\n" + options + "---\n"
        else:
            light_figure += "---\nclass: only-light-mode\n---\n"
        
        dark_options = options.replace('only-light-mode', 'only-dark-mode')
        dark_figure = "```{figure} ../_static/figures/" + dark_name + "\n"
        if dark_options:
            dark_figure += "---\n" + dark_options + "---\n"
        else:
            dark_figure += "---\nclass: only-dark-mode\n---\n"
        dark_figure += title + "\n```"
        
        return light_figure + "\n" + dark_figure
    return full_match

# Procesar archivos MD
md_files = sys.argv[1:]

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar bloques de figure con _light.svg
    pattern = r'```{figure}\s+\.\./_static/figures/(\S+_light\.svg)\s*\n(.*?)```'
    
    new_content = re.sub(pattern, convert_figure, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Procesado: {md_file}')
