#version 330 core

uniform vec3 clr;

out vec4 color;

void main()
{
	color = vec4(clr[0], 0.0f, 0.0f, 1.0f);
}
