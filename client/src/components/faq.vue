<template>
  <div class="card-body">
    <div>
      <div class="close-modal">
        <a @click="$router.go(-1)">
          <font-awesome-icon style="font-size: 140%" icon="times" />
        </a>
      </div>
      <h2 style="border-bottom: 1px solid var(--border)">
        Preguntas Frecuentes
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
    specialised concepts they handle in their day-to-day work.
    <div class="final"></div>
  </div>
</template>

<style scoped>
h4 {
  border-bottom: 1px solid var(--border);
  margin-top: 7%;
  margin-bottom: 7%;
}

.card-body {
  background-color: var(--first-color);
  text-align: left;
  padding: 8%;
}
.final {
  padding: 8%;
  margin-bottom: 15px;
}
</style>