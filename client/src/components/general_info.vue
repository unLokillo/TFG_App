<template>
  <div class="card-body">
    <div>
      <div class="close-modal">
        <a @click="$router.go(-1)">
          <font-awesome-icon style="font-size: 140%" icon="times" />
        </a>
      </div>
      <h2 style="border-bottom: 1px solid var(--border)">Información</h2>
    </div>
    <p>
      Pescaneo es una aplicación que permite la captura y valoración de
      neologismos en el ámbito de la descarbonización. Se enmarca en el
      proyecto IoTerm, desarrollado por profesoras del Departamento de
      Lingüística Aplicada a la Ciencia y la Tecnología de la Universidad
      Politécnica de Madrid en colaboración con el grupo de investigación
      Ateneo-NeoUsal de la Universidad de Salamanca. <br />
      <br />
      El objetivo principal de este proyecto es implicar a las expertas y
      expertos tecnólogos en la identificación, recogida y valoración de nuevos
      términos en el ámbito del Internet de las Cosas, de una manera
      colaborativa y lúdica.
      <br /><br />
      Con ayuda de esta flota de “pescadoras y pescadores de términos”
      pretendemos detectar, analizar, valorar y recopilar los neologismos
      terminológicos que surgen en el ámbito de la descarbonización en inglés y en español.
      <br />
      <br />
      <strong style="align-content: center"> ¿Te vienes de pesca? </strong>
    </p>
    <div>
      <h2 style="border-bottom: 1px solid var(--border)">
        Preguntas Frecuentes
      </h2>
    </div>
    <h4>¿Qué es un neologismo?</h4>
    Un neologismo es cualquier palabra de la lengua que resulta novedosa, de
    algún modo, para los hablantes. Pueden ser palabras prestadas, creadas desde
    cero, pero también palabras que ya se usaban y a las que se incorporan
    nuevos significados.
    <h4>¿Qué es un término?</h4>
    Un término puede estar formado por una sola o por varias palabras, y se
    utiliza para referirse a un concepto especializado en un ámbito de
    especialidad. Por ejemplo, emisión, en el ámbito de la descarbonización,
    es un término.
    <h4>
      ¿Por qué es importante desarrollar una terminología propia en español?
    </h4>
    Porque si disponemos de una terminología bien formada en español seremos
    capaces también de comunicarnos adecuadamente en todos los niveles de
    especialidad. Si los términos están bien recogidos y definidos, y además su
    forma se adecua a las reglas del español, nos resultará mucho más fácil
    utilizarlos para comunicarnos en nuestra propia lengua. Además, trabajar en
    un ámbito de especialidad en nuestra propia lengua nos ayuda a comprenderlo
    mejor y nos permite avanzar e innovar con más autonomía y garantías.
    <h4>
      ¿Por qué es importante que los especialistas en descarbonización propongan
      y opinen sobre las palabras que usan?
    </h4>
    Creemos que si los especialistas se implican en el proceso de detección y
    generación de los neologismos propios de su ámbito tendrán muchas más
    posibilidades de incorporarlos en su comunicación especializada diaria, y
    las posibilidades de que se implanten serán mayores. Esto les ayudará a
    desenvolverse profesionalmente con más solvencia y a poner nombres más
    funcionales y, en definitiva, más operativos desde un punto de vista
    cognitivo y profesional, a los conceptos especializados que manejen en su
    día a día.
    <h4>¿Qué papel desempeñan las lingüistas en todo este proceso?</h4>
    Las profesionales del lenguaje y la terminología se encargan de ordenar y
    sistematizar la información, las intuiciones y las preferencias de los
    especialistas, con el fin de devolvérselos a estos en forma de recursos
    útiles para su comunicación profesional, como glosarios y diccionarios
    especializados en diversos formatos. <br><br>
  </div>
</template>

<style scoped>
.card-body {
  background-color: var(--first-color);
  padding: 6%;
  text-align: left;
}

h4 {
  border-bottom: 1px solid var(--border);
  margin-top: 3%;
  margin-bottom: 3%;
}
</style>
