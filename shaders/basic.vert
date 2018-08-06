#version 330 core

layout(location=0) in vec3 position;
layout(location=1) in vec3 color;
layout(location=2) in vec2 tex_coords;

uniform mat4 pr_matrix;
uniform mat4 vw_matrix = mat4(1.0f);
uniform mat4 ml_matrix = mat4(1.0f);

out DATA {
    vec4 position;
    vec3 color;
    vec2 tex_coords;
} vs_out;

void main() {
    gl_Position = pr_matrix * vw_matrix * ml_matrix * vec4(position, 1.0f);
    vs_out.position = ml_matrix * vec4(position, 1.0f);
    vs_out.color = color;
    vs_out.tex_coords = tex_coords;
}