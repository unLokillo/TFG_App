<template>
    <div class="card-body">
        <div>
      <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
       <h2 style="border-bottom: 1px solid var(--border)">Información</h2>
       </div> 
       <p> Pescaneo es una aplicación que permite la captura y valoración de neologismos en el ámbito del Internet de las Cosas (IoT).
Se enmarca en el proyecto IoTerm, desarrollado por profesoras del Departamento de
Lingüística Aplicada a la Ciencia y la Tecnología de la Universidad Politécnica de Madrid en
colaboración con el grupo de investigación Ateneo-NeoUsal de la Universidad de Salamanca. <br> <br>
El objetivo principal de este proyecto es implicar a las expertas y expertos tecnólogos en la
identificación, recogida y valoración de nuevos términos en el ámbito del Internet de las Cosas,
de una manera colaborativa y lúdica.
<br><br>
Con ayuda de esta flota de “pescadoras y pescadores de términos” pretendemos detectar,
analizar, valorar y recopilar los neologismos terminológicos que surgen en el ámbito del IoT en
inglés y en español.
<br> <br>   
    
        <strong style="align-content:center;"> ¿Te vienes de pesca? </strong>
        </p>
    <div></div> 
    </div>    
</template>

<style scoped>
.card-body{
  background-color: var(--first-color);
  display: flex;
  padding: 4%;
  text-align: left;
  flex-direction: column;
  justify-content: space-between;
}
</style>
