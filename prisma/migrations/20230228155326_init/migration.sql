-- CreateTable
CREATE TABLE "users" (
    "id" SERIAL NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "email" TEXT NOT NULL,
    "username" TEXT,
    "password" TEXT NOT NULL,

    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "addresses" (
    "id" SERIAL NOT NULL,
    "userID" INTEGER NOT NULL,
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
CREATE UNIQUE INDEX "users_email_key" ON "users"("email");

-- CreateIndex
CREATE INDEX "addresses_userID_idx" ON "addresses"("userID");

-- CreateIndex
CREATE INDEX "indication_types_addressId_idx" ON "indication_types"("addressId");

-- CreateIndex
CREATE INDEX "indications_indicationTypeId_idx" ON "indications"("indicationTypeId");

-- AddForeignKey
ALTER TABLE "addresses" ADD CONSTRAINT "addresses_userID_fkey" FOREIGN KEY ("userID") REFERENCES "users"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "indication_types" ADD CONSTRAINT "indication_types_addressId_fkey" FOREIGN KEY ("addressId") REFERENCES "addresses"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "indications" ADD CONSTRAINT "indications_indicationTypeId_fkey" FOREIGN KEY ("indicationTypeId") REFERENCES "indication_types"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
