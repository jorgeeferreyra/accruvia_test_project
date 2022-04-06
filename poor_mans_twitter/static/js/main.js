window.$app = new Vue({
    el: '#app',
    data: () => ({
        sending: false,
        loading: false,
        form: {
            username: '',
            message: ''
        },
        tweets: []
    }),

    computed: {
        api_url() {
            return `${window.location.protocol}//${window.location.host}/api`; 
        },

        csrf_token() {
            return $('[name="csrf_token"]').attr('content');
        },

        // Let me assume that the username must be greater than or equal to 3 characters length
        // and less than or equal to 20 characters length
        // and also the tweet must be greater than or equal to 4 characters length
        // because only requirement that mentions is has to be less than or equal to 50 characters length
        validation_error() {
            const username_length = this.form.username.length;
            const message_length = this.form.message.length;

            const errors = [];

            if (username_length < 3) 
                errors.push('The Name must be greater than or equal to 3 characters length');
            else if (username_length > 20)
                errors.push('The Name must be less than or equal to 20 characters length');

            if (message_length < 4) 
                errors.push('The Tweet must be greater than or equal to 4 characters length');
            else if (message_length > 50)
                errors.push('The Tweet must be less than or equal to 50 characters length');

            return errors.length > 0
                ? errors.join('\r\n')
                : null;
        },

        validation_pass() {
            return this.validation_error === null;
        }
    },

    async mounted() {
        try {
            this.loading = true;

            const { latest_tweets } = await Promise.resolve($.get(`${this.api_url}/tweets`));

            this.tweets = latest_tweets;
        }
        catch(error) {
            alert('Ups! Something went wrong. Please contact the developer.. :(');
            console.error(error);
        }
        finally {
            this.loading = false;
        }
    },

    methods: {
        async sendTweet() {
            try {
                this.sending = true;

                if (!this.validation_pass)
                    throw new Error(this.validation_error);

                const form = Object.assign({
                    csrfmiddlewaretoken: this.csrf_token
                }, this.form);

                const { new_tweet } = await Promise.resolve($.post(`${this.api_url}/tweets/store`, $.param(form)));

                this.tweets = [new_tweet].concat(this.tweets);

                this.form.username = '';
                this.form.message = '';
            }
            catch(error) {
                if (error.message)
                    alert(error.message);
                console.error(error);
            }
            finally {
                this.sending = false;
            }
        }
    }
})