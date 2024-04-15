<template>
  <div>
    <h2>Edit Activity</h2>
    <form @submit.prevent="submit_form" method="post" action="">
      <input type="hidden" name="csrfmiddlewaretoken" :value="csrf_token">
      <p>
        <label for="id_name">Name:</label>
        <input type="text" name="name" v-model="activity_dico.name" maxlength="100" required id="id_name">
      </p>
      <p>
        <label for="id_price">Price:</label>
        <input type="number" name="price" v-model="activity_dico.price" min="0" step="0.01" required id="id_price">
      </p>
      <p>
        <label for="id_destination">Destination:</label>
        <select name="destination" v-model="activity_dico.destination" id="id_destination" required>
          <option v-for="destination in destinations" :value="destination.id">{{ destination.name }}</option>
        </select>
      </p>
      <button type="submit" class="btn btn-primary" :disabled="submitting_form">Submit</button>
    </form>
  </div>
  <br><br>
</template>

<script>
export default {
  name: 'ActivityEdit',
  data() {
    return {
      csrf_token: ext_csrf_token,
      activity_dico: ext_activity_dict,
      destinations: ext_destinations,
      submitting_form: false,
    };
  },
  methods: {
    submit_form(){
      this.submitting_form = true;
      const form = document.createElement('form');
      form.setAttribute('method', 'post');
      const form_data = {
        'csrfmiddlewaretoken': this.csrf_token,
        'name': this.activity_dico.name,
        'price': this.activity_dico.price,
        'destination': this.activity_dico.destination,
      };
      for (let key in form_data) {
        const html_field = document.createElement('input');
        html_field.setAttribute('type', 'hidden');
        html_field.setAttribute('name', key);
        html_field.setAttribute('value', form_data[key]);
        form.appendChild(html_field);
      }
      document.body.appendChild(form);
      form.submit();
    },
  },
}
</script>
