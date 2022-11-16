-- CreateTable
CREATE TABLE "addresses" (
    "id" SERIAL NOT NULL,
    "userId" INTEGER NOT NULL,
    "address" TEXT NOT NULL,

    CONSTRAINT "addresses_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "indication_types" (
    "id" SERIAL NOT NULL,
    "addressId" INTEGER NOT NULL,
    "type" TEXT NOT NULL,

    CONSTRAINT "indication_types_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "indications" (
    "id" SERIAL NOT NULL,
    "indicationTypeId" INTEGER NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "indications" INTEGER NOT NULL,

    CONSTRAINT "indications_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "addresses_userId_address_key" ON "addresses"("userId", "address");

-- CreateIndex
CREATE UNIQUE INDEX "indication_types_type_addressId_key" ON "indication_types"("type", "addressId");

-- AddForeignKey
ALTER TABLE "addresses" ADD CONSTRAINT "addresses_userId_fkey" FOREIGN KEY ("userId") REFERENCES "users"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "indication_types" ADD CONSTRAINT "indication_types_addressId_fkey" FOREIGN KEY ("addressId") REFERENCES "addresses"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "indications" ADD CONSTRAINT "indications_indicationTypeId_fkey" FOREIGN KEY ("indicationTypeId") REFERENCES "indication_types"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
