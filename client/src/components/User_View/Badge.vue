<template>
  <div class="badge-card-body">
    <div class="badge-card-completed">
      <b-avatar src="https://picsum.photos/300/150/?image=41"></b-avatar>
      {{ name_badge }}
    </div>

    <div class="badge-card-unfinished">
      <b-avatar src="https://picsum.photos/300/150/?image=41"></b-avatar>
      {{ name_badge }}
      <b-progress-bar :value="value" class="w-25"></b-progress-bar>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      value: 95,
      max: 100,
      id_badge: "123456",
      completed: false,
      name_badge: "Badge_1",
      completed_date: "XX/XX/XXXX",
      completion_percentage: 50,
    };
  },
};
</script>

<style>
.badge-card-body {
  width: 100%;
  height: 100%;
}
.badge-card-completed {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.badge-card-unfinished {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: 50%;
}
</style>
