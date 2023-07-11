<template>
  <b-container class="page  animate__animated animate__fadeIn">
    <h2>Authors: {{ authors.length }} {{ modal_name }}</h2>
    <h2>Books: {{ books.length }}</h2>
    <b-button v-b-modal.modal-1 id="createbutton">Add Author</b-button>

    <b-table
      striped
      hover
      :items="authors"
      :fields="fields"
      @row-clicked="onRowClicked"
    >
      <template #cell(numbooks)="row">
        {{ books.filter(item => item.author_id == row.item.id).length }}
      </template>
      <template #cell(actions)="row">
        <b-button size="sm" @click="onClickDelete(row.item.id)" class="mr-1">
          Delete
        </b-button>
      </template>
    </b-table>

    <b-modal id="modal-1" title="Add Author" hide-footer>
      <b-form-group id="input-group-1" label="Author Name:">
        <b-form-input
          placeholder="John Doe"
          required
          v-model="modal_name"
        ></b-form-input>
      </b-form-group>
      <b-button class="mt-3" @click="addAuthor()">Add</b-button>
    </b-modal>
  </b-container>
</template>
<script>
import HeartIcon from "vue-ionicons/dist/md-heart.vue";
import axios from "axios";

export default {
  components: { HeartIcon },
  data() {
    return {
      showLoader: true,
      showErrALert: false,
      tagVariants: ["primary", "success", "warning", "info", "dark", "danger"],
      authors: [],
      books: [],
      items: [
        { age: 40, first_name: "Dickerson", last_name: "Macdonald" },
        { age: 21, first_name: "Larsen", last_name: "Shaw" },
        { age: 89, first_name: "Geneva", last_name: "Wilson" },
        { age: 38, first_name: "Jami", last_name: "Carney" }
      ],
      fields: [
        {
          key: "name",
          label: "Author Name",
          sortable: true,
          sortDirection: "desc"
        },
        {
          key: "numbooks",
          label: "Number of Books",
          sortable: true,
          class: "text-center"
        },
        { key: "actions", label: "Actions" }
      ],
      // add modal
      modal_name: ""
    };
  },
  head: {
    title: "Authors"
  },
  methods: {
    getAuthors(success, error) {
      axios
        .get("http://localhost:8000/authors")
        .then(res => {
          console.log("##########authors", res);
          res.data.forEach(item => {
            this.authors.push({
              id: item.id,
              name: item.name
            });
          });
          success();
        })
        .catch(err => {
          error();
          console.log("Error fetching data " + err);
        });
    },
    getBooks(success, error) {
      axios
        .get("http://localhost:8000/books")
        .then(res => {
          console.log("##########books");
          res.data.forEach(item => {
            this.books.push(item);
          });
          success();
        })
        .catch(err => {
          error();
          console.log("Error fetching data " + err);
        });
    },
    addAuthor() {
      axios
        .post("http://localhost:8000/authors", {
          id: 0,
          name: this.modal_name
        })
        .then(response => {
          console.log(response.data);
          window.location.reload();
          // this.$bvModal.hide("his.$bvModal.hide()");
        })
        .catch(error => {
          console.log(error);
        });
    },
    onRowClicked(items) {
      console.log(items);
    },
    onClickDelete(author_id) {
      axios
        .post("http://localhost:8000/authors/del/"+author_id, {
        })
        .then(response => {
          console.log(response.data);
          window.location.reload();
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  async mounted() {
    this.getAuthors(
      () => {
        this.showLoader = false;
        this.getBooks(
          () => {
            this.showLoader = false;
          },
          () => {
            this.showErrALert = true;
            this.showLoader = false;
          }
        );
      },
      () => {
        this.showErrALert = true;
        this.showLoader = false;
      }
    );
  }
};
</script>
<style scoped>
.container {
  margin-top: 120px;
}
.row {
  margin-top: 40px;
}
.spinner-border {
  margin-top: 40px;
}
.card {
  text-align: left;
  color: #000;
}
#createbutton {
  margin: 10px;
}
</style>
