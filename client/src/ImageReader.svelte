<script>
    export const name = 'image'
    export let imageURL = '';

    let files

    function ImageToString(ev) {
        if (files) {
            var file = ev.target.files[0]
            if (file.type.startsWith('image/')) {
                var reader = new FileReader()
                reader.readAsDataURL(file)
                reader.onloadend = function () {
                    imageURL = reader.result
                }
            }
        }
    }
</script>
<div>
    <input type="file" bind:files {name} accept="image/*" on:change={ImageToString} />
</div>
