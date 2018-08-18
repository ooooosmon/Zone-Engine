#version 330 core

out vec4 color;

uniform vec3 light_color;
uniform vec2 light_pos;

in DATA {
    vec4 position;
    vec3 color;
} fs_in;

void main() {
    float intensity = 1.0f / length(fs_in.position.xy - light_pos);

    float ambient_strength = 0.1f;
    vec3 ambient = ambient_strength * light_color;
    vec4 result = vec4(ambient, 1.0f);
    color = vec4(fs_in.color, 1.0f);// * intensity;
}