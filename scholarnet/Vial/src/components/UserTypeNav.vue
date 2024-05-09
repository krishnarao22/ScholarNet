<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <div class="flex bg-gray-100 p-2">
        <div class="flex w-20">
        </div>
        <div class="container flex justify-start">
            <div class="flex p-1 border-b-2 border-indigo-500">
                <RouterLink to="/student">Students</RouterLink>
            </div>
            <div class="flex p-1 border-b-2 border-indigo-500">
                <RouterLink to="/student">Students</RouterLink>
            </div>
        </div>
    </div>
</template>
