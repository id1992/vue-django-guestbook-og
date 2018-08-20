<template>
    <div>
        <form v-on:submit.prevent="create">
            <div class='inputBox shadow'>
                <input type="text" v-model='name' placeholder="이름" required>
            </div>
            <div class='inputBox shadow'>
                <input type="text" v-model='text' placeholder="내용" required>
            </div>
            <div>
                <button class="addContainer">
                    <h1 class="addLabel">완료</h1>
                </button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            name: '',
            text: ''
        }
    },
    methods: {
        create() {
            axios({
                method: 'post',
                url: '/api/guestbook/create',
                data: {
                    name: this.name,
                    text: this.text
                }
            }).then((reponse) => {
                console.log(reponse);
            }).catch((error) => {
                console.log(error)
            });

            this.$router.push('/');
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
