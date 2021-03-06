---
layout: soal
author: viridi
title: "0057"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: true
category: physics
tags: ["parallel plates", "electric field", "accelerator"]
date: 2021-03-15 13:40:00 +07
permalink: /soal/0057
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-15-parallel-plates-accelerator.md
ref: https://www.youtube.com/watch?v=MGiYJC7k4IU&t=635s
---
Terdapat dua pelat konduktor sejajar yang masing-masing memilki potensial listrik $V_L$ untuk pelat sebelah kiri (left, <x style="color: red;">merah</x>) dan $V_R$ untuk pelat sebelah kanan (right, <x style="color: blue;">biru</x>), dengan $V_L > V_R$,
serta jarak antar pelat adalah $h = 4 \ {\rm mm}$.

<svg style="display: none;">
	<style type="text/css">
	.lw1 { stroke-width: 1px; vector-effect: non-scaling-stroke; }
	.pos-charge { stroke: #a00; fill: #fcc; }
	.nol-charge { stroke: #000; fill: #ccc; }
	.neg-charge { stroke: #00a; fill: #ccf; }
	</style>
	<defs>
		<g id="arr">
			<path d="M0,0 h25 m-7,-4 l7,4 m-7,4 l7,-4" />
		</g>
		<g id="yz-plate">
			<rect x="0" y="0" width="10" height="100" />
		</g>
		<g id="yz-plate-parallel-pos-neg">
			<use xlink:href="#yz-plate" y="20" class="pos-charge lw1" />
			<use xlink:href="#yz-plate" x="90" y="20" class="neg-charge lw1" />
			<path d="M0,10 h10 m-5,-5 v10" stroke="black" />
			<path d="M90,10 h10" stroke="black" />
		</g>
		<g id="yz-plate-parallel-neg-pos">
			<use xlink:href="#yz-plate" x="90" y="20" class="neg-charge lw1" />
			<use xlink:href="#yz-plate" y="20" class="pos-charge lw1" />
			<path d="M0,10 h10 m-5,-5 v10" stroke="black" />
			<path d="M90,10 h10" stroke="black" />
		</g>
		<g id="pos-charge">
			<circle cx="10" cy="10" r="10" />
			<path d="M10,10 m-5,0 h10 m-5,-5 v10" stroke="black" />
		</g>
		<g id="neg-charge">
			<circle cx="10" cy="10" r="10" />
			<path d="M10,10 m-5,0 h10" stroke="black" />
		</g>
	</defs>
</svg>

<svg width="110" height="125" style="background: none;">
	<use xlink:href="#yz-plate-parallel-neg-pos" x="5" />
	<use xlink:href="#pos-charge" x="20" y="50" class="pos-charge" />
	<!--use xlink:href="#neg-charge" x="70" y="50" class="neg-charge" /-->
	<use xlink:href="#arr" transform="translate(65,112) rotate(0)" class="lw1" stroke="black" />
	<use xlink:href="#arr" transform="translate(45,112) rotate(-180)" class="lw1" stroke="black" />
	<foreignObject x="50" y="100" width="20" height="25">$h$</foreignObject>
</svg>

Sebuah muatan positif $q > 0$ (<x style="color: blue;">biru</x>) semula berada di dekat pelat sebelah kanan dengan kecepatan sehingga energi kinetiknya $K_i > 0$.

Dikarenakan $V_L > V_R$ maka pada ruang di antara kedua pelat akan terdapat medan listrik yang berarah dari kiri ke kanan $E = (V_L - V_R) / h$. Muatan $q$ akan mengalami gaya listrik $F_E = qE = q(V_L - V_R)/h$ yang berarah ke kanan karena $q > 0$. Dengan $F_E$ adalah satu-satunya gaya yang bekerja pada muatan, maka usaha total oleh gaya listrik adalah $W = \vec{F} \cdot \vec{s} = F_E \ h = q(V_L - V_R)/h \cdot h = q (V_L - V_R)$.

Selanjutnya dapat diperoleh bahwa $q(V_L - V_R) = K_f - K_i$, sehingga energi kinetik akhir partikel saat tiba di pelat sebelah kanan adalah

<ol type="A">
<li>$K_f > K_i$.
<li>$K_f = K_i$.
<li>$K_f < K_i$.
<li>$K_f = K_i + q(V_L - V_R)$.
<li>jawab A dan D benar.
