<template>
  <div class="card-body">
    <div>
      <div class="close-modal">
        <a @click="$router.go(-1)">
          <font-awesome-icon style="font-size: 140%" icon="times" />
        </a>
      </div>
      <h2 style="border-bottom: 1px solid var(--border)">Information</h2>
    </div>
    <p>
      Term-fishing is an application that allows to capture, describe and 
      evaluate terms in the field of sustainability. It has been developed 
      as part of the educational innovation project "Gamification strategies 
      applied to the collaborative acquisition of scientific-technical 
      vocabulary in English and Spanish", developed by professors of the 
      Universidad Politécnica de Madrid. <br />
      <br />
      The main objective of this project is to motivate students of different 
      degrees of the UPM in the acquisition of scientific-technical 
      vocabulary in the field of sustainability in a collaborative and 
      playful way. 
      <br /><br />
      With the help of this fleet of "term fishermen and fisherwomen" we aim 
      to detect, analyse, evaluate and compile terms related to 
      sustainability on campus both in English and Spanish. 
      <br />
      <br />
      <strong style="align-content: center"> Coming fishing? </strong>
    </p>
    <div>
      <h2 style="border-bottom: 1px solid var(--border)">
        Frecuent Answers and questions
      </h2>
    </div>
    <h4>What is a term?</h4>
    A term can consist of a single word or several words, and is used to refer 
    to a specialised concept in a specialised field. For example, 
    sustainability is a term.
    <h4>
      Why is it important to develop our own terminology in Spanish? 
    </h4>
    Because if we have a well-formed terminology in Spanish we will also be 
    able to communicate adequately at all levels of speciality. If the terms 
    are well collected and defined, and their form is in accordance with the 
    rules of Spanish, it will be much easier for experts to use them to 
    communicate in our own language. Furthermore, working in a specialised 
    field in our own language helps us to understand it better and allows us 
    to advance and innovate with more autonomy and guarantees. 
    <h4>
      Why is it important for students to propose and give their opinion on the 
      words they use? 
    </h4>
    We believe that if specialists -and students are, after all, experts-to-be- 
    are involved in the process of detecting and generating the terms specific 
    to their field, they will have a much greater chance of incorporating them 
    into their daily specialised communication, and the chances of them becoming 
    established will be greater. This will help them to develop professionally 
    with more solvency and to give more functional and, in short, more 
    operative names from a cognitive and professional point of view, to the 
    specialised concepts they handle in their day-to-day work. <br><br>
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
