<template>
  <b-row style="margin-left: 0;margin-right: 0;">
    <b-col md="4"> </b-col>

    <b-col md="8">
      <h2 class="intro animate__animated animate__fadeInUp animate__fast">
        Hi 👋,
        <br />I<span>'m Lucas Wang</span>.
      </h2>
      <div class="col-md-10 info">
        <p>This is project for DataCose fullstack challenge</p>
      </div>
    </b-col>
  </b-row>
</template>

<script>
import GithubIcon from "vue-ionicons/dist/logo-github.vue";
import LinkedinIcon from "vue-ionicons/dist/logo-linkedin.vue";
import TwitterIcon from "vue-ionicons/dist/logo-twitter.vue";
import FacebookIcon from "vue-ionicons/dist/logo-facebook.vue";
import YoutubeIcon from "vue-ionicons/dist/logo-youtube.vue";
import MailIcon from "vue-ionicons/dist/md-mail.vue";

export default {
  components: {
    GithubIcon,
    LinkedinIcon,
    TwitterIcon,
    FacebookIcon,
    YoutubeIcon,
    MailIcon
  },

  data() {
    return {
      avatar: require("@/assets/avatar-1.webp"),
      // ADD YOUR SOCIAL LINKS HERE 👇
      socialLinks: {
        github: "http://github.com/asaoluelijah",
        linkedin: "https://www.linkedin.com/in/asaoluelijah/",
        twitter: "https://twitter.com/asaolu_elijah",
        facebook: "https://facebook.com/asaoluelijah01",
        mail: "mailto:info4a.elijah@gmail.com",
        youtube: ""
      }
    };
  },

  head: {
    title: "Datacose⚡ - Lucas Wang",
    meta: [
      {
        hid: "description",
        name: "description",
        content:
          "Lucas Wang is an awesome front-end developer and technical writer, passionate about building solutions that works across multiple platforms with high accessibility approach. Elijah has vast knowledge in web development with over 3+ years experience in building actual products"
      },
      {
        hid: "og:title",
        name: "og:title",
        content: "Datacose ⚡ - Lucas Wang"
      },
      {
        property: "og:description",
        content:
          "Lucas Wang is an awesome front-end developer and technical writer, passionate about building solutions that works across multiple platforms with high accessibility approach. Elijah has vast knowledge in web development with over 3+ years experience in building actual products"
      },
      {
        hid: "og:image",
        name: "og:image",
        content: require("@/assets/coding.png")
      }
    ]
  },
  methods: {
    changeAvatar() {
      if (this.avatar == require("@/assets/avatar-2.webp")) {
        this.avatar = require("@/assets/avatar-1.webp");
      } else {
        this.avatar = require("@/assets/avatar-2.webp");
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.$nuxt.$loading.start();

      setTimeout(() => this.$nuxt.$loading.finish(), 500);
    });
  }
};
</script>
