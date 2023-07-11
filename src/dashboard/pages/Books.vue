<template>
  <b-container class="page  animate__animated animate__fadeIn">
    <h2>Manage Books</h2>
    <p>Authors: {{ authors.length }}, Books: {{ books.length }}</p>

    <b-row>
      <b-col lg="6" class="my-1">
        <b-button v-b-modal.modal-1 id="createbutton" variant="success"
          >Add Book</b-button
        >
      </b-col>

      <b-col lg="6" class="my-1">
        <b-form-group
          label="Filter"
          label-for="filter-input"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          class="mb-0"
        >
          <b-input-group size="sm">
            <b-form-input
              id="filter-input"
              v-model="filter"
              type="search"
              placeholder="Type to Search"
            ></b-form-input>

            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''"
                >Clear</b-button
              >
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>
    </b-row>

    <b-table
      striped
      hover
      :items="books"
      :fields="fields"
      :filter="filter"
      @filtered="onFiltered"
      :current-page="currentPage"
      :per-page="perPage"
      @row-clicked="onRowClicked"
    >
      <template #cell(author_name)="row">
        {{
          JSON.stringify(
            authors.find(author => author.id == row.item.author_id)
              ? authors.find(author => author.id == row.item.author_id).name
              : ""
          )
        }}
      </template>
      <template #cell(actions)="row">
        <b-button
          size="sm"
          @click="onClickDelete(row.item.id)"
          class="mr-1"
          variant="danger"
        >
          Delete
        </b-button>
      </template>
    </b-table>
    <b-row>
      <b-col lg="6" class="my-1"> </b-col>

      <b-col lg="6" class="my-1">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          align="fill"
          size="sm"
          class="my-0"
        ></b-pagination>
      </b-col>
    </b-row>

    <b-modal id="modal-1" title="Add Book" hide-footer>
      <b-form-group id="input-group-1" label="Book Name">
        <b-form-input
          placeholder="The Guide for Python"
          required
          v-model="add_name"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Author">
        <treeselect
          v-model="add_author"
          :multiple="false"
          :options="author_options"
        />
      </b-form-group>
      <b-form-group id="input-group-3" label="Number of Pages">
        <b-form-input
          placeholder="The Guide for Python"
          required
          v-model="add_pages"
        ></b-form-input>
      </b-form-group>
      <b-button class="mt-3" @click="addBook()">Add</b-button>
    </b-modal>
  </b-container>
</template>
<script>
import HeartIcon from "vue-ionicons/dist/md-heart.vue";
import axios from "axios";
// import the component
import Treeselect from "@riophae/vue-treeselect";
// import the styles
import "@riophae/vue-treeselect/dist/vue-treeselect.css";

export default {
  components: { HeartIcon, Treeselect },
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
          key: "title",
          label: "Title",
          sortable: true,
          sortDirection: "desc"
        },
        {
          key: "author_name",
          label: "Auhor Name",
          sortable: true,
          class: "text-center"
        },
        { key: "actions", label: "Actions" }
      ],
      filter: null,
      totalRows: 1,
      currentPage: 1,
      perPage: 5,
      //Tree select
      add_name: "",
      add_pages: 1,
      add_author: null,
      author_options: []
    };
  },
  head: {
    title: "Books"
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
            this.author_options.push({
              id: item.id,
              label: item.name
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

          this.totalRows = this.books.length;
          success();
        })
        .catch(err => {
          error();
          console.log("Error fetching data " + err);
        });
    },
    addBook() {
      axios
        .post("http://localhost:8000/books", {
          id: 0,
          title: this.add_name,
          author_id: this.add_author,
          pages: this.add_pages
        })
        .then(response => {
          console.log(response.data);
          // window.location.reload();
        })
        .catch(error => {
          console.log(error);
        });
    },
    onRowClicked(items) {
      console.log(items);
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    onClickDelete(author_id) {
      axios
        .post("http://localhost:8000/books/del/" + author_id, {})
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
  margin-bottom: 10px;
}
</style>
