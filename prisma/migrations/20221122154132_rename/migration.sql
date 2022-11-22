/*
  Warnings:

  - You are about to drop the column `userId` on the `addresses` table. All the data in the column will be lost.
  - Added the required column `userID` to the `addresses` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "addresses" DROP CONSTRAINT "addresses_userId_fkey";

-- DropIndex
DROP INDEX "addresses_userId_idx";

-- AlterTable
ALTER TABLE "addresses" DROP COLUMN "userId",
ADD COLUMN     "userID" INTEGER NOT NULL;

-- CreateIndex
CREATE INDEX "addresses_userID_idx" ON "addresses"("userID");

-- AddForeignKey
ALTER TABLE "addresses" ADD CONSTRAINT "addresses_userID_fkey" FOREIGN KEY ("userID") REFERENCES "users"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
