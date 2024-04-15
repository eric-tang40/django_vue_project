<template>
  <div>
    <h2>Edit Location</h2>
      <form @submit.prevent="submit_form" method="post" action="">
      <input type="hidden" name="csrfmiddlewaretoken" :value="csrf_token">
      <p>
        <label for="id_name">Name:</label>
        <input type="text" name="name" v-model="destination_dico.name" maxlength="100" required id="id_name">
      </p>
      <p>
        <label for="id_country">Country:</label>
        <input type="text" name="country" v-model="destination_dico.country" maxlength="100" required id="id_country">
      </p>
      <p>
        <label for="id_description">Description:</label>
        <textarea name="description" v-model="destination_dico.description" id="id_description" rows="4" cols="50"></textarea>
      </p>
      <button type="submit" class="btn btn-primary" :disabled="submitting_form">
        Submit
      </button>
    </form>
  </div>
  <br><br>
</template>

<script>

export default {
name: 'LocationEdit',
components: {},
data: function() {
    return {
        csrf_token: ext_csrf_token,
        form: ext_form,
        destination_dico: ext_destination_dict,
        activities: ext_activities,
        accommodations: ext_accommodations,
        submitting_form: false,
    }},
methods: {
    submit_form(){
        if(this.submitting_form){
            return;
        }
        this.submitting_form = true;
        var form = document.createElement('form');
        form.setAttribute('method', 'post');
        let form_data = {
            'csrfmiddlewaretoken': this.csrf_token,
            'name': this.destination_dico.name,
            'country': this.destination_dico.country,
            'description': this.destination_dico.description,
        };
        console.log("form_data", form_data);

        for(var key in form_data){
            var html_field = document.createElement('input');
            html_field.setAttribute('type', 'hidden')
            html_field.setAttribute('name', key)
            html_field.setAttribute('value', form_data[key])
            form.appendChild(html_field);
        }

        document.body.appendChild(form);
        form.submit();
    },
},
}
</script>