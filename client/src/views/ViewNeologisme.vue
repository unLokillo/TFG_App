<template>
<div class="v-neologisme-card">
  <router-link to='/'>X</router-link>
  <h1>{{ name }}</h1>
<div class="descriptions-cards">
  <div v-for="(value,index) in descriptions" :key=index>
    <b-badge pill>1</b-badge>
    {{ value.content }}
  </div>
  </div>

<div class="fuentes-cards">
  <div v-for="(value,index) in fuentes" :key=index>
    {{ value.content }}
  </div>
</div>
</div>
</template>

<script>
export default {
  data() {
    return{
      id: '987654321',
      name: 'Neologismo',
      descriptions: [
        {id:1,content:"DEscripcion A"},
        {id:1,content:"DEscripcion B"}
      ],
      fuentes: [
        {id:1,content:"DEscripcion 1"},
        {id:1,content:"DEscripcion 1"}
      ],
      img: null,
      creator: 'User_1',
      likes: 2,
      creation_date: '10/10/2010'
    }
  },
}
</script>
<style>
.v-neologisme-card{
    background-color: rgb(231, 231, 231);
    padding: 3%;
}

.fuentes-cards{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  border-top: solid black 1px;
}

.descriptions-cards{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  border-top: solid black 1px;
}

.b-badge{
  background-color: red;
}
</style>