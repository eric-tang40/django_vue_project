<template>
  <div>
    <h2>Edit/Create Accommodation</h2>
    <form @submit.prevent="submit_form" method="post" action="">
      <input type="hidden" name="csrfmiddlewaretoken" :value="csrf_token">
      <p>
        <label for="id_name">Name:</label>
        <input type="text" name="name" v-model="accommodation_dico.name" maxlength="100" required id="id_name">
      </p>
      <p>
        <label for="id_price_per_night">Price Per Night:</label>
        <input type="number" name="price_per_night" v-model="accommodation_dico.price_per_night" min="0" step="0.01" required id="id_price">
      </p>
      <p>
        <div class="cascading-dropdown">
          <div class="dropdown">
            <label for="id_destination">Countries:</label>
            <select v-model="selected" id="id_destination" required>
              <option value="">Select a Country</option>
              <option v-for="country in countries">
                  {{ country }}
              </option>
            </select>
          </div>
          <div class="dropdown">
            <span>Destinations: </span>
            <select :disabled="!selected" v-model="boom" id="id_destination" required>
              <option value="">Select a Destination</option>
              <option v-for="destination in new_destinations">
                  {{ destination }}
                </option>
            </select>
          </div>
        </div> 
      </p>
      <button type="submit" class="btn btn-primary" :disabled="submitting_form">Submit</button>
    </form>
  </div>
  <br><br>
</template>

<script>
export default {
  name: 'AccommodationEdit',
  mounted() {
    this.populateCountries();
  },
  data() {
    return {
      selected: '',
      boom:'',
      new_destinations: [],
      countries: [],
      csrf_token: ext_csrf_token,
      accommodation_dico: ext_accommodation_dict,
      destinations: ext_destinations,
      submitting_form: false,
    };
  },
  methods: {
    findCountry() {
      var destinationName = this.accommodation_dico.destination_name;
      for (const destination of this.destinations) {
          if (destinationName === destination.name) {
            return destination.country;
          }
      }
    },
    findDest() {
      var country = this.selected;
      for (const destination of this.destinations) {
          if (country === destination.country) {
            console.log(destination.name);
            return destination.name;
          }
      }
    },
    populateCountries() {
      this.selected = this.findCountry();
      this.boom = this.findDest();
      const mySet = new Set(); 
      this.destinations.forEach(destination => {
          const countryLowerCase = destination.country.toLowerCase();
          if (!mySet.has(countryLowerCase)) {
              mySet.add(countryLowerCase);
              this.countries.push(destination.country);
          }
      });
      return this.countries;
    },
    submit_form(){
      this.submitting_form = true;
      var form = document.createElement('form');
      form.setAttribute('method', 'post');
      this.destinations.forEach(destination => {
        if (this.boom === destination.name) {
          this.boom = destination.id;
        }
      });
      let form_data = {
        'csrfmiddlewaretoken': this.csrf_token,
        'name': this.accommodation_dico.name,
        'country': this.accommodation_dico.country,
        'price_per_night': this.accommodation_dico.price_per_night,
        'destination': this.boom,
      };
      for (let key in form_data) {
        let html_field = document.createElement('input');
        html_field.setAttribute('type', 'hidden');
        html_field.setAttribute('name', key);
        html_field.setAttribute('value', form_data[key]);
        form.appendChild(html_field);
      }
      document.body.appendChild(form);
      form.submit();
    },
  },
  watch: {
    selected(newVal) {
      this.new_destinations = [];
      this.destinations.forEach(destination => {
        if (destination.country === newVal) {
          this.new_destinations.push(destination.name);
        }
      });
    },
  },
}
</script>
