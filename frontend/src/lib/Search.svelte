<script lang="ts">
 import type { Book } from "./types";
 import SearchResults from "./SearchResults.svelte";

  let searchText = "";
  let books: Book[] = [];

  async function search() {
    if (searchText !== "") {
        books = await fetch(
        `http://localhost:8000/search?search_string="${searchText}"`,
        {
          method: "GET",
        }
      )
        .then((response) => response.json())
        .catch((error) => {
          console.error(error);
        });

      console.log(books);
      return books;
    }
  }
</script>

<div>
  <input type="text" bind:value={searchText} placeholder="Search..." />
  <button on:click={search}>Search</button>
</div>

{#if books.length > 0}
  <SearchResults books={books} />
{/if}
