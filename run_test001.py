from utils.utils_pinecone import initialize_chain, get_response

def main():
    chain = initialize_chain()

    response1 = get_response(chain, "what are minimum viable products?")
    response2 = get_response(chain, "what is the product company gap and how can it be solved?")

    print("Response to 'what are minimum viable products?':", response1)
    print("Response to 'what is the product company gap and how can it be solved?':", response2)

if __name__ == "__main__":
    main()
