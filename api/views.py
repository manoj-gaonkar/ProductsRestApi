from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product
from .serializer import ProductSerializer

@api_view(['GET'])
def getData(request):
    sample = {"1":"manoj","2":"kirean"}
    return Response(sample)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    productserialized = ProductSerializer(products,many=True)
    print(productserialized)
    return Response(productserialized.data)

@api_view(["POST"])
def addProducts(request):
    newproduct = ProductSerializer(data=request.data)
    if newproduct.is_valid():
        newproduct.save()
    return Response(newproduct.data)


@api_view(["DELETE"])
def deleteProduct(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response("deleted")
    except Exception as e:
        return Response({"msg":str(e)})