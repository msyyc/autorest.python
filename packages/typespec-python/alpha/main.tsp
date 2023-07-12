import "@typespec/http";
import "@azure-tools/cadl-ranch-expect";

using TypeSpec.Http;

@doc("Illustrates inheritance and polymorphic model.")
@scenarioService("/type/model/inheritance")
namespace Test.Union;

@doc("Cat")
model Cat {
  eatFish: boolean;
}

@doc("Dog")
model Dog {
  eatBone: boolean;
}

@doc("Animal")
model Animals {
  content: Cat[] | Dog[];
}

@route("/test/union")
interface Discriminated {
  @scenario
  @scenarioDoc("test")
  @get
  getAnimal(): Animals;
}
