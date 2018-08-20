<template>
    <div>
        <form v-on:submit.prevent="edit">
            <div class='inputBox shadow'>
                <input type="text" v-model='name' placeholder="이름" required>
            </div>
            <div class='inputBox shadow'>
                <input type="text" v-model='text' placeholder="내용" required>
            </div>
            <div>
                <button class="addContainer">
                    <h1 class="addLabel">확인</h1>
                </button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            id  : '',
            name: '',
            text: ''
        }
    },
    created() {
        this.id   = this.$route.params.id;
        this.name = this.$route.params.name;
        this.text = this.$route.params.text;
    },
    methods: {
        edit() {
            axios({
                method: 'put',
                url: `api/guestbook/edit/${this.id}`,
                data: {
                    name: this.name,
                    text: this.text
                }
            })
            .then((reponse) => {
                console.log(reponse);
                this.$router.push('/'); 
            }).catch((err) => {
                console.log(err.response)
            });
        }
    }
}
</script>

<style>
    input:focus {
        outline: none;
    }
    .inputBox {
        background: white;
        height: 50px;
        line-height: 50px;
        border-radius: 5px 5px 5px 5px;
        text-align: left;
        margin-bottom: 1rem;
        width: 97%;
    }
    .inputBox input {
        border-style: none;
        font-size: 0.9rem;
        /* background-color: red; */
        padding: 0 0.9rem;
        width: 100%;
        height: 100%;
    }
    .addContainer {
        background: linear-gradient(to right, #6478FB, #8763fb);
        width: 10rem;
        height: 3rem;
        border-radius: 5px 5px 5px 5px;
        text-align: center;
        line-height: 15px;
    }
    .addLabel {
        color: white;
        vertical-align: middle;
    }
</style>
