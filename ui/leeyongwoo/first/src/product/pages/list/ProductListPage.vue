<template lang="">
    <v-container class="bg-yellow-lighten-5">
        <h2>이모티콘 상품 페이지</h2>
        <div style="text-align: left; margin: 15px;">
            <router-link :to="{ name: 'ProductRegisterPage' }">
                상품 등록
            </router-link>
        </div>
        <h2 class="bg-orange-lighten-2">#인기있는 이모티콘</h2>
        <h2>``</h2>
        <v-row v-if="productList.length > 0">
            <v-col v-for="(product, index) in productList" :key=index cols="6" sm="3" md="2" lg="1.5">
                <v-card @click="goToProductReadPage(product.productId)">
                    <v-img :src="getProductImageUrl(product.productImage)" aspect-ratio="1" class="grey lighten-2">
                        <template v-slot:placeholder>
                            <v-row class="fill-height ma-0" align="center" justify="center">
                                <v-progress-circular indeterminate color="grey lighten-5"/>
                            </v-row>
                        </template>
                    </v-img>
                    <v-card-title>{{ product.productName }}</v-card-title>
                    <v-card-subtitle>{{ product.productPrice }}</v-card-subtitle>
                </v-card>
            </v-col>
        </v-row>
        <v-row v-else>
            <!-- Bootstrap 등에서 기본적으로 화면을 12개의 열로 구성함(전체 쓰겠단 소리) -->
            <v-col cols="12" class="text-center">
                <v-alert type="info">등록된 상품이 없습니다!</v-alert>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" class="text-center">
                <v-img src="@/assets/images/fixed/mario.jpg" aspect-ratio="1" class="grey lighten-2">
                    <template v-slot:placeholder>
                        <v-row class="fill-height ma-0" align="center" justify="center">
                            <v-progress-circular indeterminate color="grey lighten-5"/>
                        </v-row>
                    </template>
                </v-img>
            </v-col>
        </v-row>
    </v-container>
</template>

// npm install axios --legacy-peer-deps

<script>
// 이것은 vuex 때문에 사용 가능
import { mapActions, mapState } from 'vuex'

const productModule = 'productModule'

export default {
    components: {
        // RouterLink
    },
    computed: {
        ...mapState(productModule, ['productList']),
        pagedItems () {
            const startIdx = (this.pagination.page - 1) * this.perPage
            const endIdx = startIdx + this.perPage
            return this.productList.slice(startIdx, endIdx)
        }
    },
    mounted () {
        // console.log('ProductListPage mounted()')
        // if (this.isFirstRefresh) {
        //     window.location.reload(true)
        //     this.isFirstRefresh = false
        // }
        this.requestProductListToDjango()
    },
    methods: {
        ...mapActions(productModule, ['requestProductListToDjango']),
        getProductImageUrl (imageName) {
            return require('@/assets/images/uploadImages/' + imageName)
        },
        goToProductReadPage (productId) {
            this.$router.push({
                name: 'ProductReadPage',
                params: { productId: productId }
            })
        }
    },
    data () {
        return {
            // isFirstRefresh: true,
            headerTitle: [
                {
                    title: 'No',
                    align: 'start',
                    sortable: true,
                    key: 'productId',
                },
                { title: '상품명', align: 'end', key: 'productName' },
                { title: '상품 가격', align: 'end', key: 'productPrice' },
            ],
            perPage: 5,
            pagination: {
                page: 1,
            }
        }
    }
}
</script>
