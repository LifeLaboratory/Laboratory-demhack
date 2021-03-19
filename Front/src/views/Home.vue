<template>
  <a-row type="flex" justify="center">
    <a-col :span="20">
      <div class="box">
        <img alt="Vue logo" src="../assets/logo_demhack.png" width="50%" style="margin-top: 50px;">
        <h1 style="margin-top: 50px; margin-bottom: 50px; font-size: 32pt;">Добро пожаловать в "Интернет"!</h1>
        <a-button type="primary" class="start-button" v-on:click="toAuth" style="margin-bottom: 50px; height: 75px; font-size: 32pt;">
          Подключиться
        </a-button>
      </div>
    </a-col>
  </a-row>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  methods: {
    toAuth(e) {
      this.$router.push('/auth')
    },
  },
}
</script>
