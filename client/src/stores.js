import { writable } from 'svelte/store';

export const setModal = writable({
    showModal: false,
    component: null,
    header: null
})

export const setMessageBox = writable({
    showMessageBox: false,
    messageBoxTitle: '',
    messageBoxText: ''
})