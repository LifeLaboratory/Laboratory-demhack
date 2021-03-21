<template>
  <div class="game-container">
    <div class="top-menu">
      <div class="actual-day" style="font-size: 28pt;">
        День - {{ day }}
      </div>
    </div>

    <div class="bottom-menu">
      <a-row class="profile-game">
        <a-col :span="3">
          <a-avatar :size="64" :src="this.user.pic" style="margin: 15px;"/>
        </a-col>
        <a-col :span="24" class="stats-game" style="font-size: 14pt; padding-bottom: 15px;">
          <div>Информационное здоровье: {{user.health}}</div>
          <div>Деньги: {{user.money}}₽</div>
          <div>Очки: {{user.point}}</div>
          <div>Прожито дней: {{user.round}}</div>
          <a-button v-on:click="toProfile()" style=" float: left; font-size: 14pt; margin-top: 15px; height: 60px">В профиль</a-button>
        </a-col>
      </a-row>
    </div>

    <div class="outer" style="height:80vh; width: 100%;" v-if="descr != ''">
      <div class="inner">


        <div class="card-box">
          <div
              style="font-size: 20pt; word-wrap: break-word; padding-left: 10px; padding-right: 10px; padding-top: 50px;">
            <b v-html="descr"></b><br />

            <img :src="pic" style="margin-top: 50px; max-height: 500px; margin-bottom: 50px;"/>
          </div>
        </div>
        <div style="
            width: 70%;
            margin-left: 15%;
            background: rgba(255,255,255,0.8);
            ">
          <a-button v-for="(item, index) in this.answers"
                    style="white-space: normal; justify-content: center; width: 100%; min-height: 100px;" :disabled="dis"
                    @click="sendAnswer(item.id_event)">
            {{ item.description }}
          </a-button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import {newGame, reloadGame, sendAnswer, resumeGame} from '@/api/game'
import {getProfile} from "../api/auth";

export default {
  data() {
    return {
      dis: false,
      user: {
        name: '',
        health: 0,
        money: 0,
        point: 0,
        round: 0
      },

      pic: '',
      day: 0,
      left: '',
      right: '',
      descr: '',

      leftAction: {}

    }
  },
  methods: {
    toProfile: function () {
      this.$router.push('/start');
    },

    async startNewGame() {
      let id = this.$route.query.id
      if (!id) {
        this.$router.push({path: 'start'})
        return
      }
      this.$router.replace({id: '-1'})


      let res = await newGame(localStorage.getItem('session'), id)
      this.day = res.round
      this.descr = res.description
      this.left = res.left_answer
      this.right = res.right_answer

      this.pic = res.pic
      this.user.pic = res.person_pic
      this.user.name = res.name
      this.user.health = res.health
      this.user.money = res.money
      this.user.point = res.point
      this.user.round = res.round
      this.answers = res.answer;
      this.end_game = res.end_game;

      let profile = getProfile()
      if (profile !== false) {
        this.profileUser = profile;
        profile.then(val => {
          this.profileUser = val
          console.log("Профиль: ", this.profileUser)
          // this.user.pic = this.profileUser.pic;
          this.user.name = this.profileUser.names;
        });
      }

    },

    async resumeGame() {
      let res = await resumeGame(localStorage.getItem('session'))
      this.day = res.round
      this.descr = res.description
      this.left = res.left_answer
      this.right = res.right_answer
      this.answers = res.answer;
      this.end_game = res.end_game;

      this.pic = res.pic
      this.user.pic = res.person_pic
      this.user.health = res.health
      this.user.money = res.money
      this.user.point = res.point
      this.user.round = res.round


      let profile = getProfile()
      if (profile !== false) {
        this.profileUser = profile;
        profile.then(val => {
          this.profileUser = val
          console.log("Профиль: ", this.profileUser)
          // this.user.pic = this.profileUser.pic;
          this.user.name = this.profileUser.names;
        });
      }
    },

    async sendAnswer(ans) {
      this.dis = true
      this.pic = undefined;
      let res = await sendAnswer(localStorage.getItem('session'), ans)
      if (res.end === true) {
        this.$warning({
          title: `Вы проиграли. Прожито дней ${this.day}`
        })
        this.$router.push({path: 'start'})
      }
      console.log(res);
      console.log(res.health)
      console.log(this.user.health)
      console.log(res.health - this.user.health)

      this.day = res.round
      this.descr = res.description
      this.left = res.left_answer
      this.right = res.right_answer
      this.answers = res.answer;

      this.user.health = res.health
      this.user.money = res.money
      this.user.point = res.point
      this.user.round = res.round

      this.dis = false

      if (res.end_game === true) {
        this.answers = [];
        this.descr = "К сожалению, для вас, игра окончена!"
      }
    }

  },
  mounted() {

    let profile = getProfile()
    if (profile !== false) {
      this.profileUser = profile;
      profile.then(val => {
        this.profileUser = val
        console.log("Профиль: ", this.profileUser.pic);
        this.user.pic = this.profileUser.pic;
        this.user.name = this.profileUser.names;
      });
    }

    let type = this.$route.query.type
    if (type === 'resume') {
      this.resumeGame()
      return
    }
    this.startNewGame();
  },

};
</script>
<style>
.right {
  margin-left: 15px;
}

.left {
  margin-right: 15px;
}

.left > .ant-btn-icon-only {
  width: 64px;
  height: 64px;
}

.right > .ant-btn-icon-only {
  width: 64px;
  height: 64px;
}

.outer:before {
  content: '';
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}

.inner {
  width: 100%;
  display: inline-block;
  margin-top: 50px;
}

.outer {
  text-align: center;
}

.left, .right, .card-box {
  display: inline-block;
}

.center-menu {
  margin-top: 80px;
  width: 30%;
  margin-left: 35%;
}

.card-box {
  width: 70%;
  background: rgba(255, 255, 255, 0.8);
}

.actual-day {
  font-size: 24px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 0px 0px 5px 5px;
  width: 50%;
  top: 0px;
  margin-left: 25%;
}

.game-container {
  height: 100vh;
  width: 100vw;
}

.center-menu {
  vertical-align: middle;
}

.stats-game {
  margin-left: 30px;
  margin-top: 10px;
  text-align: left
}

.ant-progress-line {
  margin-left: 10px;
  width: 80% !important;
}

.bottom-menu {
  border: solid 1.2px black;
  border-radius: 5px 5px 0px 0px;
  left: 25%;
  width: 50%;
  min-width: 550px;
  background: rgba(255, 255, 255, 0.8);
  margin: 50px auto 0;
}

</style>
