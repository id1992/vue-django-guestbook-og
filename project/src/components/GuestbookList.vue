<template>
    <div>
        <ul>
            <li v-for="(guestbook, index) in guestbooks">
                <!-- <guestbook ></guestbook> -->
                <label id='nameLabel'> {{ guestbook.name }} </label>
                <label id='textLabel'> {{ guestbook.text }} </label>
                <span class="btns">
                    <span class="editBtn" type='button' @click="editGuestBook(index, guestbook.id, guestbook.name, guestbook.text)">
                        <i class='fa fa-pencil' aria-hidden='true'></i>
                    </span>        
                    <span class="removeBtn" type='button' @click="removeGuestbook(index, guestbook.id)">
                        <i class='fa fa-trash-o' aria-hidden='true'></i>
                    </span>        
                </span>
            </li>
        </ul>
        <button class="addContainer" v-on:click="onClickCreateGuestBookBtn">
            <h1 class="addLabel">새로운 글 남기기</h1>
        </button>
    </div>
</template>

<script>
export default {
    props: ['propsdata'],
    data() {
        return {
            guestbooks: []
        }
    },
    created() {
       this.showGuestBooks();
    },
    methods: {
        showGuestBooks() {
            console.log("showGuestBooks");
            axios({    
                method: 'get',
                url: '/api/guestbooks',
            }).then((response) => {
                let i, guestbooks;
                guestbooks = response.data.guestbooks;
                console.log(response.data)
                if (guestbooks.length > 0) {
                    for (i = 0; i < guestbooks.length; i++) {   
                        // Django 단에서 객체를 아예 전달해서
                        // 프론트는 객체 만들 필요 없이 PUSH만 하게  
                        // this.guestbooks.push(guestbooks[i]);
                        this.guestbooks.push({
                            id  : guestbooks[i].guestbook_id,
                            name: guestbooks[i].guestbook_name,
                            text: guestbooks[i].guestbook_text
                        });
                    }
                }
            }).catch((error) => {
                console.log(error);
            });
        },  
        editGuestBook(index, id, name, text) {
            this.$router.push({
                name: 'edit',
                params: {
                    'id'  : id,
                    'name': name,
                    'text': text
                }
            });
        },
        removeGuestbook(index, id) {
            axios({
                method: 'delete',
                url: `/api/guestbook/remove/${id}`
            }).then((response) => {
                this.guestbooks.splice(index, 1);
            }).catch((error) => {
                console.log(error);
            });
        },
        onClickCreateGuestBookBtn() {
            this.$router.push('create');
        }
    },
}
</script>

<style>
    ul {
        list-style-type: none;
        padding-left: 0px;
        margin-top: 0;
        text-align: left;
    }
    li {
        display: flex;
        min-height: 50px;
        height: 50px;
        line-height: 50px;
        margin: 0.5rem 0;
        padding: 0 0.9rem;
        background: white;
        border-radius: 5px;
    }
    .checkBtn {
        line-height: 50px;
        color: #62acde;
        margin-right: 5px;
    }
    .btns {
        margin-left: auto;
    }
    .editBtn {
        margin-right: 1rem; 
    }
    .removeBtn {
        color: #de4343;
    }
    .addContainer {
        background: linear-gradient(to right, #6478FB, #8763fb);
        width: 11rem;
        height: 3rem;
        border-radius: 5px 5px 5px 5px;
        text-align: center;
        line-height: 15px;
    }
    .addLabel {
        color: white;
        vertical-align: middle;
    }
    #nameLabel {
        margin-left: 0.5rem;
        width: 150px;
    }
</style>

