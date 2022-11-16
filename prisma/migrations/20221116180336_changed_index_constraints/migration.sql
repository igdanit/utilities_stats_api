-- DropIndex
DROP INDEX "addresses_userId_address_key";

-- DropIndex
DROP INDEX "indication_types_type_addressId_key";

-- DropIndex
DROP INDEX "indications_indicationTypeId_createdAt_key";

-- CreateIndex
CREATE INDEX "addresses_userId_idx" ON "addresses"("userId");

-- CreateIndex
CREATE INDEX "indication_types_addressId_idx" ON "indication_types"("addressId");

-- CreateIndex
CREATE INDEX "indications_indicationTypeId_idx" ON "indications"("indicationTypeId");
