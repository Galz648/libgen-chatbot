<!-- SearchResults.svelte -->
<script lang="ts">
  import type { Book } from "./types";

  export let books: Book[] = [];
</script>

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Author</th>
      <th>Title</th>
      <th>Publisher</th>
      <th>Year</th>
      <th>Pages</th>
      <th>Language</th>
      <th>Size</th>
      <th>Extension</th>
      <th>Mirror 1</th>
      <th>Mirror 2</th>
      <th>Mirror 3</th>
    </tr>
  </thead>
  <tbody>
    {#each books as book}
      <tr>
        <td>{book.ID}</td>
        <td>{book.Author}</td>
        <td>{book.Title}</td>
        <td>{book.Publisher}</td>
        <td>{book.Year}</td>
        <td>{book.Pages}</td>
        <td>{book.Language}</td>
        <td>{book.Size}</td>
        <td>{book.Extension}</td>
        <td><a href={book.Mirror_1}>Mirror 1</a></td>
        <td><a href={book.Mirror_2}>Mirror 2</a></td>
        <td><a href={book.Mirror_3}>Mirror 3</a></td>
      </tr>
    {/each}
  </tbody>
</table>
