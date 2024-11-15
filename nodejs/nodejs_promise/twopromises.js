let promise1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Promise 1 resolved")
    }, 6000);
})

let promise2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Promise 2 resolved")
    }, 3000);
})

// promise1.then((successMessage) => {
//     console.log("From Callback " + successMessage)

//     promise2.then((successMessage) => {
//         console.log("From Callback " + successMessage)
//     })
// })

promise1.then((successMessage) => {
    console.log("From Callback " + successMessage)
})

promise2.then((successMessage) => {
    console.log("From Callback " + successMessage)
})