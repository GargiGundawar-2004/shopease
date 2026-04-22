// wishlist.js

function addToWishlist(productId) {
    if (!productId) {
        throw new Error("Invalid product");
    }
    console.log("Wishlist updated:", productId);
}